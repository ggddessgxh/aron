import itertools
str=input("输入一个字符串:")
li=list(str)
m=list(itertools.permutations(li,len(str)))
print(m)
