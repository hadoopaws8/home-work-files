##def add(a,b,c):
##    print(a)
##    print(b)
##    return c        # if you remove 4 in perameter error
##    print(a,b,c)
##print(add(2,3,4))


##def add(a,b,c):
##    print(a)
##    print(b)
##    return c        # if you remove 4 in perameter error TypeError
##    print(a,b,c)
##print(add(2,3,4,5))

#position arguments using keywords

##def add(a,b,c):
##    print(a)
##    print(b)
##    return c    
##print(add(b=5,c=2,a=9))

###default position perameter
##def add(a,b,c=0):
##    print(a)
##    print(b)
##    return c    
##print(add(2,3))

#default position perameter
##def add(a,b,c=0):
##    print(a)
##    print(b)
##    return c    
##print(add(2,3,6))
##print("--------------------")
##print(add(2,3))

#lenth of arguments using keywor ds

##def sum(a,*b):
####    print(a)
####    print(b)
##    c=a
##    for i in b:
##        c=c+i
##    print(c)
##sum(5,6,34,78)

##def sum(*b):
####    print(a)
####    print(b)
##    c=0
##    for i in b:
##        c=c+i
##    print(c)
##sum(5,6,34,78)

### keyworded variable lengh Arguments
##def person(name,**data):     # keyword with argument using **
##    print(name)             #here data is a dictionary
##    print(data)
##    for i,j in data.items():
##        print(i,j)
##
##person('jaya',age=30,city="chittor",mob=990058)


# keyworded variable lengh Arguments
def person(**data):     # keyword with argument using **
                 #here data is a dictionary
    print(data)
    for i,j in data.items():
        print(i,j)

person(name='jaya',age=30,city="chittor",mob=990058)

