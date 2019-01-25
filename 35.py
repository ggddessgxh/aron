n=input("请输入一个五位整数:")
li=list(n)
if li[0]==li[4] and li[1]==li[3]:
    print("是回文数")
else:
    print("不是回文数")
