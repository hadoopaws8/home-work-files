l=[]
n=int(input("enter the number of list elements: "))
for i in range(n):
    l.append(int(input("enter the next element: ")))
print(l)
l1=[]
for j in range(n):
    l1.append(int(input("enter the next element: ")))
print(l1)
l.sort()
l1.sort()
c=l+l1
f=set(c)
if l==l1:
    print("both list are identical lists")
else:
    print("lists are different")

for i in f:
    if ((i in l) or (i in l1)) and c.count(i)!=1:
        print(i,":",c.count(i))
k=[]
for j in f:
    if c.count(j)==1:
        k.append(j)
print("the distinct elements are given : ",k)
            
    
