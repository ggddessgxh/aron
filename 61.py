li=list(map(int,input("输入三个数:").split(",")))
li.sort(reverse=True)
for i in li:
    print(i,end=" ")
