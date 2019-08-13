###generator
##def my_gen():
##    n=1
##    print("this is printed first")
##    #generator function contains yield statements
##    yield n
##
##    n+=1
##    print("this is printed second")
##    yield n
##
##    n+=1
##    print("this is printed at last")
##    yield n
##p=my_gen()
##print(p)
##print(next(p))
##print(next(p))
##print(next(p))
###print(next(p))   # this goes to error that is StopIteration


###generator with loop
##
##def rev_str(my_str):
##    length = len(my_str)
##    for i in range(length-1, -1, -1):
##        yield my_str[i]
###for loop to reverse the string
##for char in rev_str("Hello"):
##    print(char)


##my_list =[1,3,6,10]
###print([x**2 for x in my_list])
###print((x**2 for x in my_list)) # this is generator 
##a=(x**2 for x in my_list)
##print(a)
##print(type(a))
##print(next(a))
##print(next(a))
##print(next(a))
##print(next(a))
###print(next(a)) #out of index the error is StopIteration
##print("------------------------")
##print(sum(x**2 for x in my_list))
##print(max(x**2 for x in my_list))


def all_even():
    n=0
    while True:
        yield n
        n+=2
p=all_even()
print(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))



