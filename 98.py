import random
L=[]
for i in range(2):
    n1=random.randint(48,57)#0~9之间的数字
    L.append(chr(n1))
for j in range(1):
    n2=random.randint(65,90)#大写字母
    L.append(chr(n2))
    n3=random.randint(97,122)#小写字母
    L.append(chr(n3))
Y=" ".join(L)
print(Y)
