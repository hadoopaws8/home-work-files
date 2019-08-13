##try:
##    s="Hi python, Hello python"
##    print("start")
##    s.index("java",0,len(s))
##    print("email")
##except Exception as e:
##    print(e)
##print("bye")


##try:
##    s="Hi python, Hello python"
##    print("start")
##    #a=abc
##    1/0
##    print("email")
##except Exception as e:
##    print(e)
##print("bye")

# specific exception hadling
##try:
##    s="Hi python, Hello python"
##    print("start")
##    a=abc
##    #1/0
##    print("email")
##except NameError as e:
##    print(e)
##print("bye")


## #specific exception hadling
##try:
##    s="Hi python, Hello python"
##    print("start")
##    #a=abc
##    1/0
##    print("email")
##except ZeroDivisionError as e:
##    print(e)
##print("bye")

###all errors exception hadling using Exception keyword
##try:
##    s="Hi python, Hello python"
##    print("start")
##    #a=abc
##    1/0
##    print("email")
##except Exception as e:
##    print(e)
##print("bye")

#multiple except but it handle one only hadling because you are not having multiple try commands
try:
    s="Hi python, Hello python"
    print("start")
    1/0
    #a='abc    syntax error not handile in file but in idl we can hadle
    a=abc
    print("email")
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
print("bye")
