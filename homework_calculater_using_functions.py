def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floardiv(a,b):
    return a//b
def powerof(a,b):
    return a**b

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("------------------------------------------------------------------")
print("   addition= +        subraction= -         divition= /")
print("multiplication= *   floor_division= //    exponent of= **")
print("------------------------------------------------------------------")
choice=input("enter your choice of the symbol: ")
if choice=="+":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice =="-":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice =="*":
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice =="/":
    if num2>0:
        print(num1,"/",num2,"=",div(num1,num2))
    else:
        print(num1,"number not divisiable by",num2)
elif choice =="//":
    if num2>0:
        print(num1,"//",num2,"=",floardiv(num1,num2))
    else:
        print(num1,"number not divisiable by",num2)
elif choice =="**":
    print(num1,"**",num2,"=",powerof(num1,num2))
else:
    print("please enter proper choice")
    
