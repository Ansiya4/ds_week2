# -_-_-_-_-_MEAN-_-_-_-_-_[1.a]

list1=[83,70,70,63,70,70]

def mean(list):
    return sum(list) / len(list)
print("Mean=",mean(list1))

# -_-_-_-_-_Using Numpy Module-_-_-_-_-_[1.b]
import numpy as np
list1=[83,70,70,63,70,70]
mean1= np.mean(list1)
print("Mean=",mean1)