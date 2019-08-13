import time
import sys
                    #carage return \r not working in idl it work in pycham

##for i,j in enumerate(range(100)):
##    print("hi jayaram "+str(i), end="\r")
##    time.sleep(1)
##    

##for i in range(10):
##    print("\rhi jayaram"),


##for i in range(20):
##    time.sleep(0.5)
##    print("\rnumber{0}",format(i),end="")
##    sys.stdout.flush()

for i in range(10):
    print("\rjayaram "+str(i),end="")
    time.sleep(0.5)
