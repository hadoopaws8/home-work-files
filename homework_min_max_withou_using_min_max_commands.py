#l=[20,30,50,70]
l=[20,100,50,10,80,70]
##m=0
##for i in l:
##    if m<i:
##        m=i
##print("maximum value: ",m)
##
##k=l[0]
##for i in l:
##    if k>i:
##        k=i
##print("minimum value:",k)

j=0
k=l[0]
for i in l:
    if j<i:
        j=i
    if k>i:
        k=i
print("maximum value: ",j)
print("minimum value:",k)
