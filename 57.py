n=int(input("please input n:"))
L= [1]
for i in range(n):
    print((n-i)*" ",L,"\n")
    L.append(0)
    L = [L[j] + L[j-1]for j in range(i+2)]
