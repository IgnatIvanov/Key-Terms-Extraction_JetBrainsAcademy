in_string = str(input())
for letter in in_string:
    if not letter.isalpha():
        break
    else:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            print('vowel')
        else:
            print('consonant')
