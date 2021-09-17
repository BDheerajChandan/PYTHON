''' Write a program in Python to shift all zeros in a list to an end.'''
N=7
arr=[1,2,0,3,0,4,5,0,6]
a=[]
for i in arr:
    if i!=0:
        a.append(i)
for i in arr:
    if i==0:
        a.append(i)
arr=a
print(arr)