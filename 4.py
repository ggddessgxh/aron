p_list = [0,31,59,90,120,151,181,212,243,273,304,334]
r_list = [0,31,60,91,121,152,182,213,244,274,305,335]
str1 = input("请输入年月日：")
a, b, c = str1.split('.')
a = int(a)
b = int(b)
c = int(c)
def f(str1):
    if (a % 100 == 0 and a % 400 == 0) or (a % 100 != 0 and a % 4 == 0):
        return r_list[b-1]+c
    else:
        return p_list[b-1]+c
print(f(str1))
