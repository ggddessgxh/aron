s=eval(input("请输入3*3的矩阵:"))
a_list=list(s)
for i in a_list:
    print(i)
sum=0
for j in range(3):
    for k in range(3):
        b_list=a_list[j]
        S=b_list[k]
        if j==k:
            sum=sum+S
print("主对角线元素之和为",sum)
