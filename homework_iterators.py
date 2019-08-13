l=iter([1,2,3,4,5])
##print(l.__next__())
##print(l.__next__())
##print(l.__next__())
##print(l.__next__())
##print(l.__next__())
##print(l.__next__())
count=0
while True:
    print(l.__next__())
    count+=1
    if count>4:
        break
