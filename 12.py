import math
n=int(input())
m=math.log(n,3)
if 3**m==n:
    print("是3的幂次方")
else:
    print("不是3的幂次方")
