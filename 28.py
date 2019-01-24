a=2
b=3
c=1
d=2
counter=18
s=a/c+b/d
while counter>0:
    b=a+b
    a=b
    d=c+d
    c=d
    m=b/d
    s+=m
    counter-=1
print(s)

    
