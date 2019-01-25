n=int(input())
a=0
for i in range(2,n,1):
    for m in range(2,i,1):
        if i%m==0:
            break
    else:
        a+=1
print(a)
