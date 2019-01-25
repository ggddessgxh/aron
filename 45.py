a=eval(input("请输入第一个3行3列矩阵:"))
A=list(a)
b=eval(input("请输入第二个3行3列矩阵:"))
B=list(b)
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]
for k in C:
    print(k)

        
