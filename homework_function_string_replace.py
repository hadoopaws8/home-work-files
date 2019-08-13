s="Hi python, Hello python"
c=s.count("python")
def replace(a,b):
    print(b.join(s.split(a,c)))

replace("python","Java")
