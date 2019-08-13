
try:
    var = open(r'C:\Users\jaya\Desktop\calculater\jaya1.txt','r')
    print(var.read())
except Exception as e:
    print(e)
    
print("bye")
