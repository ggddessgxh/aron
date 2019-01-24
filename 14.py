m=0
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        m+=1
        print(i)
print(m)          
