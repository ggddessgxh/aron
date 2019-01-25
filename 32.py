def f(x):
   if x == -1:
       return ''
   else:
        return str[x] + f(x-1)

str = input("请输入一个字符串:")
print(f(len(str)- 1))

