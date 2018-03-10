fruitfile = open ("fruits.txt")
fruitstr=fruitfile.read()
fruitfile.close()
fruitstr = fruitstr.splitlines()
for i in fruitstr:
    strleng=str(i)
    print(len(strleng))
