l=[]
n=int(input("enter the number of elements in a list: "))
for i in range(n):
    l.append(i)
print(l)

print("the second last index is : ",l[-2])
print("the third last index is :",l[-3])

print(len(l)-3)
print(len(l)-2)
