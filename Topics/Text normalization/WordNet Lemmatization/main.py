from nltk.stem import WordNetLemmatizer


# your code here
lemmatizer = WordNetLemmatizer()
word = str(input())
print(lemmatizer.lemmatize(word, pos='n'))
print(lemmatizer.lemmatize(word, pos='a'))
print(lemmatizer.lemmatize(word, pos='v'))
