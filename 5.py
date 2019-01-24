x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
if x<y:
    a=x
    x=y
    y=a
if x<z:
    a=x
    x=z
    z=a
if y<z:
    a=y
    y=z
    z=a
print(x,y,z)
