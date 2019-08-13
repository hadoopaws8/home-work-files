#var = open("C:\\Users\\jaya\\Desktop\\calculater\\jaya1.txt",'r')

try:
    print("start")
    var = open("C:\\Users\\jaya\\Desktop\\calculater\\jaya1.txt",'r')
    print("hi")
except FileNotFoundError as e:
    print(e)
