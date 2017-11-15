#Andrew Parker
#11/15/17
#longestWord.py - prints longest word

words = input('Enter some words: ').split(' ')
words.sort()

if len(words)%2 == 0:
        print(words[mid:mid+2])
else: 
        print(words[mid+1])



