# -_-_-_-_-_RANGE-_-_-_-_-_[4.a]
def range(list1):
    maximum=max(list1)
    minimum = min(list1)
    range = maximum - minimum
    return range

list1=[1,2,1,2,3,4,3]
print("Range=",range(list1))