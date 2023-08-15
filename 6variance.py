# -_-_-_-_-_VARIANCE-_-_-_-_-_[5.a]
list1=[1,2,1,2,3,4,3]

def variance(list1):
    mean = sum(list1)/len(list1)
    sum1=0
    for num in list1:
        num = (num-mean)**2
        sum1 += num
    variance = sum1/len(list1)
    return variance

print(variance(list1))

# -_-_-_-_-_Using Numpy Module-_-_-_-_-_[5.b]
import numpy as np
var = np.var(list1)
print(var)