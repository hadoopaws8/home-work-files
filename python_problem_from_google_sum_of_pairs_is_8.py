a=[1,2,3,4,4,6]
b={}
l=[]
for i in a:
    for j in a:
        if i+j==8:
            b[i]=j
            print(i,j)
for i,j in b.items():
    l.append(i)
    l.append(j)
print(l)
