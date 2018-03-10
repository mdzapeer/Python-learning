numbers = [1, 2, 3]
numberfile = open("numbers.txt", "w")
for i in numbers:
    numberfile.write(str(i)+"\n")
