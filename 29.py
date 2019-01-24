s=1
sum=0
for i in range(1,21):
    for m in range(1,i+1):
        s*=m
        sum+=s
print(sum)
