#Andrew Parker
#11/13/17
#middleWord.py - prints middle word

words = input('Enter some words: ').split(' ')
mid = len(words)//2

if len(words)%2 == 0:
        midWords = words[mid:mid+1]
else: 
        midWords = words[mid]

print(midWords)
    

