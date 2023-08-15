# # -_-_-_-_-_MODE-_-_-_-_-_[2.a]

# list1=[1,2,1,2,3,8,4,3,1,2]
# def mode(list1):
#     count={}
#     for num in list1:
#         if num in count:
#             count[num]+=1
#         else:
#             count[num]=1
#     print(count,"..............")
#     print(count.items(),".....item")
#     mode = [num for num,ctr in count.items() if max(count.values())==ctr]
#     return mode
# print("Mode=",mode(list1))

# -_-_-_-_-_Using Statistics Module-_-_-_-_-_[2.b]
import statistics as ss
list1=[1,2,1,2,3,4,3]
mode1 = ss.multimode(list1)
print("Mode=",mode1)