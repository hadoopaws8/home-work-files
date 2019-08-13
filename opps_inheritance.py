##class father:
##    car="BMW"
##    bankbalence="4 Milliance"
##    def bussiness(self):
##        return "airline"
##class son(father):
##    pass
##obj=son()
##print(obj.car)
##print(obj.bankbalence)
##print(obj.bussiness())


##            #method overwriting
##class father:
##    car="BMW"
##    bankbalence="4 Milliance"
##    def bussiness(self):
##        return "airline"
##    def to_marry(self):
##        print("kritti")
##class son(father):
##    def to_marry(self):
##        print("sonu")
##obj=father()
##obj1=son()
##print(obj.car)
##print(obj.bankbalence)
##print(obj.bussiness())
##obj.to_marry()
##obj1.to_marry()

##                #lenth of arguments
##def add(a,*args):
##    print(a)
##    x,y,z= args
##    print(x,y,z)
##add(2,4,3,6)


            #encapsulation
class father:
    __car="BMW"
    __bankbalence="4 Milliance"
    def __bussiness(self):
        return "airline"
    def to_marry(self):
        print("kritti")
##    def display(self):
##        print(self.__car)
##        print(self.__bankbalence)
    
class son(father):
    pass
##    def to_marry(self):
##        print("sonu")
obj=father()
obj1=son()
#obj.display()
#obj1=son()
print(father._father__car)
print(son._father__car)
print(obj._father__bankbalence)
print(obj._father__bussiness())
obj.to_marry()
#obj1.to_marry()
print(dir(father))

