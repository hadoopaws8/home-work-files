
#data write

##var = open(r'C:\Users\jaya\Desktop\calculater\jaya2.txt','w')
##l=int(input("enter the number : "))
##data="jayaram\n"*l
##dat=var.writelines(data)
##var.close()


##var = open(r'C:\Users\jaya\Desktop\calculater\jaya2.txt','w')
##l=int(input("enter the number : "))
##data="jayaram\n"*l
##dat=var.writelines(data)
##var1=open(r'C:\Users\jaya\Desktop\calculater\jaya2.txt','r')
##readdata=var1.readlines()
##print(type(readdata))
##for i in readdata:
##    print(i)
##var.close()


###append data to file
##var = open(r'C:\Users\jaya\Desktop\calculater\jaya2.txt','a')
##l=int(input("enter the number : "))
###d=input("enter the data:")
##data="jayaram\n"*l
##dat=var.writelines(data)
##var.close()

with open(r'C:\Users\jaya\Desktop\calculater\jaya2.txt','w') as f:
    f.writelines(["jaya\n","sonu\n","dood\n","ram"])
    print(f.closed)
print(f.closed)
