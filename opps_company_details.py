class company:
    company_name="TATA"
    bike_weels=2
    car_weels=4
    truck_weels=6
    def __init__(self,vehical,name,model,color):
        self.nm=name
        self.mo=model
        self.cl=color
        self.vehi=vehical
    def display(self):
        print("\t\t  Company Name: ",company.company_name)
        print("\t\t  --------------------")
        if self.vehi=="bike":
            print("\tBike Name:",self.nm,"\t\tweels: ",company.bike_weels)
            #print("weels: ",company.bike_weels)
        elif self.vehi=="car":
            print("\tCar Name :",self.nm,"\t\tweels: ",company.car_weels)
           # print("weels: ",company.car_weels)
        elif self.vehi=="truck":
            print("\tTruck Name: ",self.nm,"\t\tweels: ",company.truck_weels)
           # print("weels: ",company.truck_weels)
        print("\tModel: ",self.mo,"\t\t\tColour: ",self.cl)
        #print("Colour: ",self.cl)
#print("Company Name: ",company.company_name)    
vc=company("bike","Hero Honda",2012,"Blue")
vc.display()
print()
print()
vc1=company("car","Benz",2018,"Red and Blue Mixer")
vc1.display()
print()
print()
vc2=company("truck","Eicher",2019,"Brown")
vc2.display()
