def returnval(a,b,c):
    print("before")
    add=a+b
    yield add
    sub=b-a
    yield sub
    mul=a*c
    yield mul
p=returnval(2,8,4)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(p)
print(type(p))
