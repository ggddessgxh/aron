def sw(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sw(n-1) + sw(n-2)

n = int(input())
print(sw(n))
