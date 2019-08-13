s="Hi python Hello python by python"
k=0
for i in range(4):
    k=s.find('python',k,len(s))
    
    if k ==-1:
        break
    print(k)
    k+=1
   
