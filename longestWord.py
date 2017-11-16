#Andrew Parker
#11/15/17
#longestWord.py - prints longest word

words = input('Enter some words: ').split(' ')

word = "" 

i = 0
for w in words:
    length = len(w)
    if length > i:
        i = length
print(w)
