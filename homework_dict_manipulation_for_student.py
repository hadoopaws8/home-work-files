stu_record=[{'name':'Rom','subject':'python','score':80,'year':2016},
            {'name':'Rom','subject':'python','score':60,'year':2017},
            {'name':'Rom','subject':'python','score':90,'year':2018}]

stu_data={}
year=[]
score=0
count=0
for i in stu_record:
    if i['name']=='Rom':
        score+=i['score']
        year.append(i['year'])
        count+=1
        
for j in stu_record:
    if j['name']=='Rom' and j['subject']=='python':
        stu_data['name']=j['name']
        stu_data['subject']=j['subject']
        stu_data['score']=score
        stu_data['year']=year
        stu_data['Avg']=score//count
##print(score)
##print(year)
print(stu_data)
#print(count)
