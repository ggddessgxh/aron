a=[0,2,3,4,5,0,6,0,7]
k=0
for i in range(len(a)):
    if a[k]==0:
        a.append(a.pop(k))
    else:
        k+=1
print(a)

