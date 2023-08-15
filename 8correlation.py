# -_-_-_-_-_CORRELATION-_-_-_-_-_[8.a]
import math

hour = [1,2,3,4,5,6]
w_loss=[1.5,2.25,3.375,5.0625,7.59375,11.390625]

def correlation(list1,list2):
    leng = len(list1)
    mean_list1 = sum(list1)/len(list1)
    mean_list2 = sum(list2)/len(list2)
    sums = sum((list1[i]-mean_list1) * (list2[i]-mean_list2) for i in range(leng))
    sq_root = math.sqrt((sum(((list1[i]-mean_list1)**2) for i in range(leng)) * sum(((list2[i]-mean_list2)**2) for i in range(leng))))
    cor = sums/sq_root
    return cor

print(correlation(hour,w_loss))

# -_-_-_-_-_Using Numpy Module-_-_-_-_-_[8.b]
import numpy as np
cor = np.corrcoef(hour,w_loss)[0,1]
print(cor)