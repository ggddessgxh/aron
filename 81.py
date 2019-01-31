n=(input("输入四位数:"))
list=[]
for i in range(4):
    m=(int(n[i])+5)%10
    list.append(m)
list.reverse()
print(list)
