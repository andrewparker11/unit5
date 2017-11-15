#Andrew Parker
#11/15/17
#dictionaryDemo.py - lists practice

dictionary = ['alphabet','sweatshirt','sweatpants','shorts','computer','waterbottle']

dictionary.sort()

number = int(input('What number word do you want to look up? '))
if number>len(dictionary):
    print(number, 'is an invalid choice')
else:
    print('Word number', number, 'is', dictionary[-1])