d={'Rom':40,'Sohan':40,'Rohan':50}
d1=d.copy()
for i in d.keys():
    if d[i]==40:
        d1.update({'jayaram':d1.pop(i)})
    elif i=="Rohan":
        d1[i]=80
    
print(d1)
