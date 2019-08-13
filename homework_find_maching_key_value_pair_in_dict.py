d1={'k1':20,'k2':40,'k3':50}
d2={'k1':80,'k2':40,'k5':80}
s=[]
s1={}
for i in d1.items():
    if i in d2.items():
        #print(i)
        s.append(i)
        s1[s[0][0]]=s[0][1]  #d.items() return tuple of list of tuple 
#print(s)
#print(dict(s))
#print(s1)
#print(s[0][0])
print(s1)
