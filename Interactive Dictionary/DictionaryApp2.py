import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def inputcasecheck(userin):
    if userin.title() in data:
        return (extractj(userin.title()))
    elif userin.upper() in data:
        return (extractj(userin.upper()))
    else:
        return (extractj(userin.lower()))

def partmatch (word):
    word=str(word[0])
    userin=input ("Did you want to see the meaning for '%s' \nYes or No?\n" %word)
    userin=userin.lower()
    if userin == "yes" or userin == "y":
        return (data[word])
    elif userin == "no" or userin == "n":
        userin2=input ("Enter the word: \n")
        return inputcasecheck(userin2)
    else:
        while userin != "yes" or userin != "y" or userin != "no" or userin != "n":
            userin=input ("Please enter 'yes' or 'no': ")
            if userin == "no" or userin == "n":
                userin3=input ("Enter the word: \n")
                if userin.title() in data:
                    return (extractj(userin.title()))
                elif userin.upper() in data:
                    return (extractj(userin.upper()))
                else:
                    return (extractj(userin3.lower()))
            if userin == "yes" or userin == "y":
                return (data[word])

def extractj (userin):
    out=difflib.get_close_matches(userin, data.keys(), 1)
    if userin in data:
        return (data[userin])
    elif len(out)>0:
        out2=difflib.get_close_matches(userin, data.keys())
        print ("Closest matches to %s: \n" %userin + str(out2))
        return partmatch(out)
    else:
        return ("Word not in dictionary\n")

userin=input ("\nEnter a word: \n")
#if userin[0].isupper():
#   output1=(extractj(userin))
#Alternative solution using title()

output1=inputcasecheck(userin)

if type(output1) == list:
    for item in output1:
        print(item)
else:
    print(output1)
