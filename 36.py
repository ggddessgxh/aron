a=input("输入第一个字母:")
if a=="M":
    print("周一")
elif a=="W":
    print("周三")
elif a=="F":
    print("周五")
elif a=="T":
    b=input("输入第二个字母:")
    if b=="u":
        print("周二")
    else:
        print("周四")
else:
    b=input("输入第二个字母:")
    if b=="u":
        print("周日")
    else:
        print("周六")
