fruitfile = open ("fruits.txt")
fruitstr=fruitfile.read()
fruitfile.close()
fruitstr = fruitstr.splitlines()
for i in fruitstr:
    print(len(i))
