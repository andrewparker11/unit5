#Andrew Parker
#11/13/17
#middleWord.py - prints middle word

words = input('Enter some words: ').split(' ')
dictionary = [words]

mid = len(words)//2

if len(words)%2 == 0:
        print(words[mid:mid+1]
else: 
        print(words[mid])


