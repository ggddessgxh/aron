m=eval(input("输入当月利润(万元):"))
a=int()
if m<=10:
  a=m*0.1
elif m<=20 and m>10:
    a=10*0.1+(m-10)*0.075
elif m<=40 and m>20:
    a=10*0.1+10*0.075+(m-20)*0.05
elif m<=60 and m>40:
    a=10*0.275+(m-40)*0.03
elif m<=100 and m>60:
    a=10*0.335+(m-60)*0.015
else:
    a=10*0.395+(m-100)*0.01
print(a)
