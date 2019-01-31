n = int(input('请输入人数：'))
list1 = list(range(1, n + 1))
count=0
while len(list1) > 1:
    list2 = list1[:]
    for i in range(0, len(list2)):
        count = count + 1
        if count % 3 == 0:
            list1.remove(list2[i])

print('最后留下的是原来的第 {} 号。'.format(list2[0]))
