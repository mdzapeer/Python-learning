def ctof(cel):
        if cel >= -273.15:
            fahren=cel*(9/5)+32
            return fahren
        else:
            return ("Temperature lower than physically possible")

temperatures=[10,-20,-289,100]

for t in temperatures:
    print (ctof(t))
