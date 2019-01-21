for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                    m=a*1000+b*100+c*10+d
                    print(m)
