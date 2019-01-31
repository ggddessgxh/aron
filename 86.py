fa=open("A.txt","rt")
x=fa.read()
fa.close()

fb=open("B.txt","rt")
y=fb.read()
fb.close()

fc=open("C.txt","w")
L=list(x+y)
fc.write(L.sort())
fc.close
