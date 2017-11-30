#Andrew Parker
#11/17/17
#warmup15.py - gets list of numbers and makes x2 list

def doubled(x):
    for x in x:
        x[0] = 2*x[0]
        x[1] = 2*x[1]
        x[2] = 2*x[2]

print(doubled([2,4,6]))