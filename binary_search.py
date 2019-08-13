                #binary search
                #binary search will work when list is sorted else not work
                #mid index of value is graterthan search value u=mid or l=mid
pos=-1
def search(list1,n):
    l=0
    u=len(list1)-1
    while l<u:
        mid=(l+u)//2
        if list1[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<n:
                l=mid
            else:
                u=mid
    return False

list1=[5,1,7,6,2,10,15,3]
list1.sort()
n=2

if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
