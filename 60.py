n=int(input("请输入整数:"))
r=~n
if -2147483648<n<2147483647:
    print(r)
else:
    print("数值溢出")

