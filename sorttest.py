#Andrew
#11/15/17
#sorting.py - code to test a sorting function

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(L):
    pos = 0
    while pos < len(L):
        if pos == 0 or L[pos] >= L[pos-1]:
            pos = pos + 1
        else:
            L[pos], L[pos-1] = L[pos-1], L[pos]
            pos = pos - 1
    return L 
    
    
    
    
"""
 procedure gnomeSort(a[]):
    pos := 0
    while pos < length(a):
        if (pos == 0 or a[pos] >= a[pos-1]):
            pos := pos + 1
        else:
            swap a[pos] and a[pos-1]
            pos := pos - 1
    return L 
"""

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
