def f(n):
    if n%2==0:
        s=0
        for i in range(1,n):
            if i*2>n:
                break
            else:
                s=s+(1/(i*2))
        return s
    else:
        s=0
        for j in range(1,n):
            if j*2-1>n:
                break
            else:
                s=s+(1/(j*2-1))
        return s
        
n=int(input())
print(f(n))
