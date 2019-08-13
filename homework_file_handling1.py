
##var = open(r'C:\Users\jaya\Desktop\calculater\jaya.txt','r')
##data=var.readlines()
##use_access=int(input("enter the number of line you want see: "))
##c=len(data)
##
##if use_access>c:
##    print("this is not a proper index ")
##else:
##    print(data[use_access-1])


try:
    var = open(r'C:\Users\jaya\Desktop\calculater\jaya.txt','r')
    data=var.readlines()
    use_access=int(input("enter the number of line you want see: "))
    c=len(data)
    if use_access>c:
        print("this is not a proper index ")
    else:
        print(data[use_access-1])
except Exception as e:
    print(e)




