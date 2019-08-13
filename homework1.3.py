l=['a','b','c','d']
for i in range(4):
    for j in range(4):
        print(l[i],end="")
        if j<3:
            print("|",end="")
    print()
