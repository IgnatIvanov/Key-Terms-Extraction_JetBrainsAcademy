from collections import OrderedDict
import nltk

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
        if '</value>' in line:
            text += line.removesuffix('</value>\n')
            is_text_reading = False
            for token in nltk.tokenize.word_tokenize(text.lower()):
                frequency_dict.setdefault(head, {})  # Setting empty dictionary as default
                buffer_dict = frequency_dict[head]  # Reading previous frequency data for current token
                buffer_dict.setdefault(token, 0)  # Setting 0 count as default for token
                buffer_dict[token] += 1  # Calculating appearance frequency for current tail
                frequency_dict[head] = buffer_dict
            text_list = nltk.tokenize.word_tokenize(text.lower())
            # Hand-made sorting algorithm
            frequency_dict[head] = OrderedDict(sorted(frequency_dict[head].items(), reverse=True))
            answer_dict = {}
            max_value = max(frequency_dict[head].values())
            while len(answer_dict) < 5:
                for x in frequency_dict[head].items():
                    if x[1] == max_value:
                        answer_dict[x[0]] = x[1]
                max_value -= 1
            print(*[*answer_dict][:5])
        else:
            string = line.removeprefix('      <value name="text">')
            string = string.removeprefix('          ')
            string = string.removesuffix('\n')
            text += ' ' + string

file.close()
