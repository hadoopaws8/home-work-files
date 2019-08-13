l1=[1,4,6,8,6,2,8,1]
l2=[1,3,1,4,6,6]
l3=l1+l2
print("l3",l3)
l2=set(l2)
print("l2",l2)
print("l1",l1)
for i in l1:
    if i in l2:
        print(i,":",l3.count(i))
    else:
        print(i,"This element is not repeat in list")
