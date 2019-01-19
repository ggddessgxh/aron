t=99
print("前一百中的素数为:",end=' ')
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            t=t-1
            break
    else:
         print(i,end=' ')
print("个数为:",t)
