# -_-_-_-_-_MEDIAN-_-_-_-_-_[3.a]
list1=[1,3,4,2,6,5]
def median(list1):
    list1.sort()
    n = len(list1)
    if n%2!=0:
        median = list1[n//2]
    else:
        median = (list1[(n//2)-1] + list1[(n//2)])/2
    return median
print(median(list1))

# -_-_-_-_-_Using Numpy Module-_-_-_-_-_[3.b]
import numpy as ss
list1=[1,3,4,2,6,5]
median = ss.median(list1)
print("Median=",median)