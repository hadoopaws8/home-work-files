d1={'k1':20,'k2':40,'k3':50}
d2={'k1':80,'k2':40,'k5':80}
s={}
for i in d1.keys():
    for j in d2.keys():
        if i==j:
            s[i]=d1[i]+d2[j]
for i in d1.keys():
    if i not in d2.keys():
        s[i]=d1[i]
for i in d2.keys():
    if i not in d1.keys():
        s[i]=d2[i]
print(s)
