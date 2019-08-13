l=[]
n=int(input("enter the number of list elements: "))
for i in range(n):
    l.append(int(input("enter the next element: ")))
print(l)

for j in range(len(l)):
    for k in range(j+1,len(l)):
        if l[j]>l[k]:
            l[j],l[k]=l[k],l[j]
print(l)
