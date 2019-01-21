import math
for x in range(1,10000):
    i=int(math.sqrt(x+100))
    k=int(math.sqrt(x+168))
    if i**2==x+100 and k**2==x+168:
        print(x)
