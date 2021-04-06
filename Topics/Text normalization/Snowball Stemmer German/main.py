from nltk.stem import SnowballStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

# write your code here
snow = SnowballStemmer('german')
for word in sent:
    print(snow.stem(word))
