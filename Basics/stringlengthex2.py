def stringlength(stringvar):
    if type(strinput) == int:
        return "this int is not a string"
    elif type(strinput) == float:
        return "this float is not a string"
    else:
        return len(stringvar)

strinput=int(input("Enter a string: "))
print (stringlength(strinput))
