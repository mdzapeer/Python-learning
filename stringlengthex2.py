def stringlength(stringvar):
    return len(stringvar)

strinput=int(input("Enter a string: "))
if type(strinput) == str:
    print (stringlength(strinput))
else:
    print("this is not a string")
