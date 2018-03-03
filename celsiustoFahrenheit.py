def ctof(cel):
        if cel >= -273.15:
            fahren=cel*(9/5)+32
            return fahren
        else:
            return ("Temperature lower than physically possible")

celinput=input ("Enter Celsius to convert to Fahrenheit: ")
print (ctof(float(celinput)))
