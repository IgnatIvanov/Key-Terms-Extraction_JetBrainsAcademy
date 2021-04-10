import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

file = open('news.xml', 'r')  # Opening XML file to reading
is_text_reading = False  # Flag to remember text reading state
text = ''
head = ''
frequency_dict = {}  # Dictionary for storing frequencies of news tokens
vectorizer = TfidfVectorizer()  # Vectorizer for TF-IDF
corpus = []  # List of all documents
doc_words_count = {}

for line in file:
    if 'value name="head"' in line:
        head = line
        head = head.removeprefix('      <value name="head">')
        head = head.removesuffix('</value>\n')
        head += ':'

    if '<value name="text">' in line:
        text = ''
        is_text_reading = True

    if is_text_reading:
        if '</value>' in line:  # Calculating statistics below
            text += line.removesuffix('</value>\n')
            text = text.replace("'", ' ')
            text = text.replace("-", ' ')
            is_text_reading = False
            for_corpus_text = ""
            for token in nltk.tokenize.word_tokenize(text.lower()):
                # Flags for remember if a current element is stopword or punctuation symbol
                doc_words_count.setdefault(head, 0)  # Setting empty dictionary as default
                doc_words_count[head] += 1
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
                    for_corpus_text += str(token + ' ')
            corpus.append(for_corpus_text)

        else:
            string = line.removeprefix('      <value name="text">')
            string = string.removeprefix('          ')
            string = string.removesuffix('\n')
            text += ' ' + string

# TF-IDF calculating
vectorizer.fit(corpus)
for doc in frequency_dict.items():
    for word in doc[1].items():
        if '-' in word[0]:
            frequency_dict[doc[0]][word[0]] *= 0
        elif len(word[0]) == 1:
            frequency_dict[doc[0]][word[0]] *= 0
        else:
            frequency_dict[doc[0]][word[0]] *= vectorizer.idf_[vectorizer.vocabulary_[word[0]]] / doc_words_count[head]

# Printing statistics for all documents
for head in frequency_dict.keys():
    # Hand-made sorting algorithm
    print(head)
    frequency_dict[head] = dict(sorted(frequency_dict[head].items(), reverse=True))
    answer_dict = {}
    for max_value in sorted([x for x in frequency_dict[head].values()], reverse=True)[:5]:
        for x in frequency_dict[head].items():
            if x[1] == max_value:
                answer_dict[x[0]] = x[1]
            if len(answer_dict) >= 5:
                break
    print(*[*answer_dict][:5])

file.close()
