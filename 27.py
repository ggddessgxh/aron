import itertools
for i in itertools.permutations("xyz"):
    if i[0] != "x" and i[1] != "x" and i[2] != "z":
         print("a vs" ,i[0], "\n","b vs",i[1],"\n", "c vs",i[2])
