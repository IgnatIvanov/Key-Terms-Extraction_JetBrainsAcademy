import nltk


# the line below reads a sentence from the input and converts it into a list
sent = input().split()

# your code here

# nltk.download('averaged_perceptron_tagger')  # download the tagger
print(nltk.pos_tag(sent))
