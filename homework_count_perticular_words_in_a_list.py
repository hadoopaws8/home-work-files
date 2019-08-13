s=["shown","Exception","Error","error of the first line","exception of second line","error is last line"]
s1=""

for i in s:
    s1=s1+i+" "

s2=s1.lower()
print(s2)
strings=["exception","error"]
for i in strings:
    k=0
    j=0
##    print(i)
##    print("the word",i," in list")
    while k!=-1:                        #here -1 is last word index using s2.find()
        k=s2.find(i,k,len(s2))
        if k!=-1:
            #print(k)
            k+=1
            j+=1
    #print(s2)
    print("The number ",i," word in a string is: ",j)

