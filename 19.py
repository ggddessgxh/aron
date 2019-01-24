n=eval(input("please input:"))
str="{:032b}".format(n)
a_list=[]
a_list=list(str)
a_list.reverse()
for i in a_list:
    print(i,end="")
