n=input("输入一个整数:")
print("这是一个%d位数"%len(n))
list_a=list(n)
list_a.reverse()
for i in list_a:
    print(i,end="")
