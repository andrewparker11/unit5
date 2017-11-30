#Andrew Parker
#11/17/17
#warmup15.py - gets list of numbers and makes x2 list

def doubled(x):
    y = []
    for i in x:
        y.append(2*i)
    return y
print(doubled([2,4,6]))