List1=list(map(int,input().split(",")))
print(List1)
List2=[]
k=eval(input("输入非负数k:"))
n=len(List1)
for i in range(-k,n-k):
    List2.append(List1[i])
print(List2)

