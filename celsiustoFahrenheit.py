def ctof(cel):
        fahren=cel*(9/5)+32
        return  fahren

celinput=input ("Enter Celsius to convert to Fahrenheit: ")
print (ctof(float(celinput)))
