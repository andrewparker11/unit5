#Andrew Parker

#biggest

def biggest(x):
    y = []
    for i in x:
        if x[0]>x[1] and x[0]>x[2]:
            biggest = x[0]
        if x[1]>x[0] and x[1]>x[2]:
            biggest = x[1]
        if x[2]>x[1] and x[2]>x[0]:
            biggest = x[2]
    return biggest
print(biggest([2,4,6]))