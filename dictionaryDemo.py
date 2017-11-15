#Andrew Parker
#11/15/17
#dictionaryDemo.py - list practice 

words = input('Enter some words: ').split(' ')

dictionary = ['alphabet','sweatshirt','sweatpants','shorts','computer','waterbottle']

dictionary.sort()

number = int(input('What number word do you want to look up? '))
print('Word number', number, 'is', dictionary[-1])