                #linear search if element is match that display found and position

pos=0
def search(list1,n):
    i=0
    while i<(len(list1)):
        if list1[i]==n:
            globals()["pos"]=i
            return True
        i+=1
    return False
list1=[5,8,2,7,10,1,25]
n=10

if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
