s=str(input("请输入一些字符:"))
fp=open("file.txt","w")
for i in s:
    if i=="#":
        break
    else:
        fp.write(i)
fp.close()
