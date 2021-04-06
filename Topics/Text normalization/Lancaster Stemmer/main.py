from nltk.stem import LancasterStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

# write your code here
lancaster = LancasterStemmer()
for word in sent:
    print(lancaster.stem(word))
