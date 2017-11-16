#Andrew Parker
#11/16/17
#warmup13.py - makes list of random numbers and prints min max and sum

from ggame import *
from random import randint

numbers = []
for i in range(1,21):
    numbers.append(randint(1,20))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
    





