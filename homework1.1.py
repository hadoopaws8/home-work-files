l=['a','b','c','d']
for i in range(4):
    for j in range(4):
        print(l[j],end="")
    print()
    if i<3:
        print("------")
