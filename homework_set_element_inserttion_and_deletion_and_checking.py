s=set()
n=int(input("enter the number of elements in set: "))
for i in range(n):
    s.add(int(input("enter next element of set: ")))
check=int(input("enter which element you want check: "))
if check in s:
    print(check,"your element in set so i am deleted from set ")
    s.discard("check")
else:
    print(check,"element is not present in set")
    
