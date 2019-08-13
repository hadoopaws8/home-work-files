stu_score={'student1':60,'student2':80,'student3':90,'student4':40,'student5':100}
scr={}
score=[]
for i in stu_score.values():
    score.append(i)
score.sort()
a=score[-2]
b=score[-1]
for j in stu_score.keys():
    if stu_score[j]==a or stu_score[j]==b:
        scr[j]=stu_score[j]
print(stu_score)
print("Top two score are: ",scr)
