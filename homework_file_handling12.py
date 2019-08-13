var = open(r'C:\Users\jaya\Desktop\calculater\jaya.txt','r')
data=var.readlines()
use_access=int(input("enter the number of line you want see: "))
c=len(data)

if use_access>c:
    print("this is not a proper index ")
else:
    del(data[use_access-1])
for i in data:
    print(i)


##var1= open(r'C:\Users\jaya\Desktop\calculater\jaya1.txt','w')
##l=["BTM\n","jpnager\n","silk","jaya"]
##dat=var1.writelines(l)
##var1.close()
