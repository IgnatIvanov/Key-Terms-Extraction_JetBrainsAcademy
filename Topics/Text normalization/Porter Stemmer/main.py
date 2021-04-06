from nltk.stem import PorterStemmer


porter = PorterStemmer()
print(porter.stem(str(input())))
