d1={'k1':20,'k2':40,'k3':50}
d2={'k1':80,'k2':40,'k5':80}
for i,j in d1.items():
    for p,k in d2.items():
        if i==p:
            print(i,":",j)
            print(p,":",k)
