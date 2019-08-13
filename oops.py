##class stu:
##    def __init__(self):
##        print("inside the function")
##        self.name="sid"
##        self.age=25
##        self.course="python"
##print("before")
##obj=stu()
##print("after")
##print(obj.name)
##print(obj.age)
##print(obj.course)
##print("##########################")
##obj1=stu()
##print(obj1.name)
##print(obj1.age)
##print(obj1.course)

##class stu:
##    def __init__(self,name,age,course):
##        print("inside the function")
##        self.nm=name
##        self.ag=age
##        self.cur=course
##print("before")
##obj1=stu("jaya",30,"python")
##print(obj1.nm,obj1.ag,obj1.cur)
##print("########################")
##obj2=stu("ram",28,"linux")
##print(obj2.nm,obj2.ag,obj2.cur)
##print("end")
##
##print(dir(obj1))


##class stu:
##    def __init__(self,name,age,course):
##        print("inside the function")
##        self.nm=name
##        self.ag=age
##        self.cur=course
##    def display(self):
##        print(self.nm)
##        print(self.ag)
##        print(self.cur)
##print("before")
##obj1=stu("jaya",30,"python")
##obj1.display()
##print("#####################")
##obj2=stu("ram",28,"linux")
##obj2.display()

                    #class object create
##class stu:
##    count=0
##    def __init__(self,name,age,course):
##        print("inside the function")
##        self.nm=name
##        self.ag=age
##        self.cur=course
##        #stu.count=stu.count+1
##        stu.count+=1
##        #self.cou=stu.count
##    def display(self):
##        print(self.nm)
##        print(self.ag)
##        print(self.cur)
##        #print(self.cou)
##print("before")
##obj1=stu("jaya",30,"python")
##obj1.display()
###print(obj1.cou)
##print(stu.count)
##print("#####################")
##obj2=stu("ram",28,"linux")
##obj2.display()
###print(obj2.cou)
##print(stu.count)

                        #class method
class stu:
    count=0
    course_fee=2000
    def __init__(self,name,age,course):
        print("inside the function")
        self.nm=name
        self.ag=age
        self.cur=course
        #stu.count=stu.count+1
        stu.count+=1
        self.cou=stu.count
    def display(self):
        print(self.cou,self.nm,self.ag,self.cur)
    @classmethod
    def discount(cls,disc):
        cls.fee=cls.course_fee -((cls.course_fee)*disc/100)
        print("course fee:",cls.fee)
obj1=stu("jaya",30,"python")
obj1.display()
stu.discount(10)
print("#####################")
obj2=stu("ram",28,"linux")
obj2.display()
stu.discount(10)


