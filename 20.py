n=eval(input("please input n:"))
for n in range(1,n+1):
    if n%3==0 and n%5!=0:
        print("Fizz",end=" ",)
    elif n%3!=0 and n%5==0:
        print("Buzz",end=" ",)
    elif n%3==0 and n%5==0:
        print("FizzBuzz",end=" ")
    else:
        print(n,end=" ")
    

