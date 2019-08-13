##def add(a,b):
##    print(a+b)
##add(2,3)
##print(add(2,3))
##
##def add(a,b):
##    print(a+b)
##    return 4
##print(add(2,3))

##def add(a,b):
##    return a+b
##p=add(2,3)
##print(p)


##def add(a,b):
##    print("before")
##    return a              # first return work allways after the code will be terminate
##    print("after")      #another programs are error but it will work for one return
##    return b
##p=add(2,3)
##print(p)


def add(a,b):
    return a,b    #don't use multiple values in return that is ded code manager will sclod
p=add(2,3)
print(p)

