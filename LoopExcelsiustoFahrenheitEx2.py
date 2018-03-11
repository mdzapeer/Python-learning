def ctof(cel):
        if cel >= -273.15:
            fahren=cel*(9/5)+32
            return (str(fahren)+"\n")
        else:
            return ("")

temperatures=[10,-20,-289,100]

with open("temps.txt", "w") as tempsfile:
    for t in temperatures:
        tempsfile.write(ctof(t))
