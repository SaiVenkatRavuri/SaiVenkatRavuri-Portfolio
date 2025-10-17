# a=102
# result=str(a)
# print(type(result))
# g={1,2,3,4}
# print(type(g))
# h={1:'one',2:'two',3:'three'}
# print(type(h))
# i=True
# print(type(i))
# j=False
# print(type(j))
# k=None
# print(type(k))
# number=[1,2,3]
# print(number)
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     if a>c:
#         print('a is big')
#     else:
#         print('c is big')
# elif b>c:
#     print('b is big')
# else:
#     print('c is big')
# string='Sai Venkat'
# l=len(string)
# i=0
# while i<10:
#     print(string[i],end="")
#     i=i+2
"""
string=input()
l=len(string)
cnt=0
i=0
while i<l:
    if string[i]=='':
        cnt+=1
    i+=1
print('Number of words are : ',cnt+1)
"""
# Abstaraction
'''
from abc import ABC, abstractmethod
class Cars(ABC):
    def wheels(self):
        print("4 wheels")
    @abstractmethod
    def steering(self):
        pass
class Tata(Cars):
    def steering(self):
        print("Power Steering")
class Mahi(Cars):
    def steering(self):
        print("Normal steering")
tata=Tata()
mahi=Mahi()
print("TATA CAR")
print("========")
tata.wheels()
tata.steering()
print("MAHINDRA CAR")
print("========")
mahi.wheels()
mahi.steering()

'''

# input : 10 20 30 40 1 6 100 200
# 200
# list_of_items=list(map(int,input().split()))
#print(max(list_of_items))
# m=list_of_items[0]
# lg=len(list_of_items)
# i=1
# while i<lg:
#     if list_of_items[i]>m:


# Perform addition operation on the items which does not have digit zero.
# In the above input there are items without zero are 
# 1 6 7
list_of_items = list(map(int, input().split()))
s = 0
for i in list_of_items:
    if '0' not in str(i):
        s += i
print(s)