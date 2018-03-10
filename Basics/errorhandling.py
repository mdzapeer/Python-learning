print ("This will divide 2 numbers")
try:
    a = int(input ("Enter First Number: "))
    b = int(input ("Enter Second Number: "))
    print("The result is:", a/b)
except ValueError:
    print ("Only numbers")
except ZeroDivisionError:
    print ("Not possible")
