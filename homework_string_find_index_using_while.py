s="Hi python Hello python by python"
k=0
while k !=-1:
    k=s.find('python',k,len(s))
    if k !=-1:
        print(k)
        k+=1
   
