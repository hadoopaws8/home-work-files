# keyworded variable lengh Arguments
def person(**data):     # keyword with argument using **
                 #here data is a dictionary
    print(data)
    for i,j in data.items():
        print(i,j)

person(name=input("enter your name: "),age=int(input("enter your age: ")),city="chittor",mob=990058)
