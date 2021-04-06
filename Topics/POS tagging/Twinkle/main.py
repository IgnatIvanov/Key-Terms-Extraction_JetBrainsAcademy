import nltk

# nltk.download('averaged_perceptron_tagger')

poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

for word in nltk.pos_tag(poem):
    if word[1] == 'NN':
        print(word[0])
