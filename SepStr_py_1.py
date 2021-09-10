# Write a program to split into sentence into words.

print("ENTER THE STRING: ")
s=input()
st=s.split()
print("\n")
for i in st:
	print(i,end='\n')

'''

ALTERNATE PROGRAM :


print("ENTER THE STRING : ")
s=input()
s=s+" "
st=""
print("\n")
for i in s:
    if i==' ':
        print(st,end='\n')
        st=""
    else:
        st=st+i
'''