##try:
##    print("before")
##    1/0
####except Exception as e:
####    print("Exeption block")     #which block is first that first hadling
####    print(e)
##except ZeroDivisionError as e:
##    print("zero division block")
##    print(e)
##    print(type(e))
##except Exception as e:
##    print("Exeption block")
##    print(e)
##print("end")
    

##try:
##    print("before")
##    1/0
##    print("abc")
##    
##except Exception as e:                  # finally is allways work 
##    print(e)
##    print(type(e))
##finally:
##    print("inside finally")
##print("bye")


try:
    print("before")
   # 1/0
    print("abc")
                                        #even except is not there finally is work
finally:
    print("inside finally")
print("bye")
