def f(x):
    for i in x:        
        if x.count(i)==1:
            return x.find(i)
    return -1

x=input("给定一个字符串：")

print(f(x))

