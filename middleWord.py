#Andrew Parker
#11/13/17
#middleWord.py - prints middle word

words = input('Enter some words: ').split(' ')
dictionary = [words]

mid = len(words)//2 -1

if len(words)%2 == 0:
        print(words[mid:mid+2])
else: 
        print(words[mid+1])


