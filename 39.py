for i in range(1,101):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        print(i)
