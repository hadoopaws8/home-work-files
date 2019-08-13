l=[]
n=int(input("enter the number of elements in a list: "))
for i in range(n):
    l.append(int(input("enter next element: ")))
print("the list elements are :",l)
k=[]
j=len(l)-1
for i in range(len(l)):
    k.append(l[j-i])
print("the reverse list is: ",k)
