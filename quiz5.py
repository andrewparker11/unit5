#Andrew Parker

#biggest

def biggest(x):
    for i in x:
        if x[0]>x[1] and x[0]>x[2]:
            biggest = x[0]
        if x[1]>x[0] and x[1]>x[2]:
            biggest = x[1]
        if x[2]>x[1] and x[2]>x[0]:
            biggest = x[2]
    return biggest
print(biggest([2,4,6]))




y = []
def rand5():
    y.append('randint(0,101)')
    
print(rand5())
        
"""
#rand5
from random import randint


def rand5(x):
    i = 0
    y = []
    while y<6:
        y.append('randint(0,101)')
    i = i + 1
print(rand5())
        
"""

#lastElement

def last(x):
    lastE = last[-1]
    return lastE

print(last(['cat','dog','rat']))


