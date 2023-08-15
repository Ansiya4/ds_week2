# -_-_-_-_-_STANDARD DEVIATION-_-_-_-_-_[6.a]
list1=[83,70,70,63,70,70]

from  math import sqrt
def standard_deviation(list1):
    mean = sum(list1)/len(list1)
    sum1=0
    for num in list1:
        num = (num-mean)**2
        sum1 += num
    variance = sum1/len(list1)
    s_d = sqrt(variance)
    return s_d

print(standard_deviation(list1))

# -_-_-_-_-_Using Numpy Module-_-_-_-_-_[6.b]

import numpy as np
s_d = np.std(list1)
print(s_d)