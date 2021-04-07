from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk import WordNetLemmatizer


nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

file = open('news.xml', 'r')  # Opening XML file to reading
is_text_reading = False  # Flag to remember text reading state
text = ''
head = ''
frequency_dict = {}  # Dictionary for storing frequencies of news tokens
for line in file:
    if 'value name="head"' in line:
        head = line
        head = head.removeprefix('      <value name="head">')
        head = head.removesuffix('</value>\n')
        head += ':'
        print(head)

    if '<value name="text">' in line:
        text = ''
        is_text_reading = True

    if is_text_reading:
        if '</value>' in line:  # Calculating statistics below
            text += line.removesuffix('</value>\n')
            is_text_reading = False
            for token in nltk.tokenize.word_tokenize(text.lower()):
                # Flags for remember if a current element is stopword or punctuation symbol
                bool_stopword = False
                bool_punctuation = False
                bool_not_noun = False
                lemmatizer = WordNetLemmatizer()
                token = lemmatizer.lemmatize(token)

                # Checking on stopwords and punctuations
                if token in stopwords.words('english'):
                    bool_stopword = True
                if token in list(punctuation):
                    bool_punctuation = True
                # print(*nltk.pos_tag([token]))
                # print([token])
                if nltk.pos_tag([token])[0][1] != 'NN':
                    bool_not_noun = True

                if bool_punctuation or bool_stopword or bool_not_noun:  # If something was found
                    pass  # Do nothing
                else:  # Add the current element to an answer
                    frequency_dict.setdefault(head, {})  # Setting empty dictionary as default
                    buffer_dict = frequency_dict[head]  # Reading previous frequency data for current token
                    buffer_dict.setdefault(token, 0)  # Setting 0 count as default for token
                    buffer_dict[token] += 1  # Calculating appearance frequency for current tail
                    frequency_dict[head] = buffer_dict

            # Hand-made sorting algorithm
            # frequency_dict[head] = OrderedDict(sorted(frequency_dict[head].items(), reverse=True))
            frequency_dict[head] = dict(sorted(frequency_dict[head].items(), reverse=True))
            answer_dict = {}
            max_value = max(frequency_dict[head].values())
            # print(max_value)
            while len(answer_dict) < 5:
                for x in frequency_dict[head].items():
                    if x[1] == max_value:
                        answer_dict[x[0]] = x[1]  # Add the current element to an answer
                max_value -= 1
            print(*[*answer_dict][:5])
            # print(frequency_dict[head])
        else:
            string = line.removeprefix('      <value name="text">')
            string = string.removeprefix('          ')
            string = string.removesuffix('\n')
            text += ' ' + string

file.close()
