def f(a,b):
    z=[]
    for i in a:
        for j in b:
            if i==j:
                z.append(i)
    return z
                 
a=[1,2,3,4,5,6]
b=[1,7,8,9,0,3]
print(f(a,b))
                
