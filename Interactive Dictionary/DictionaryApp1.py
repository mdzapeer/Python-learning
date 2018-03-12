import json
import difflib
from difflib import get_close_matches

def extractj (userin):
    data=json.load(open("data.json"))
    out=difflib.get_close_matches(userin, data.keys(), 1)
    if userin in data:
        return (data[userin])
    elif len(out)>0:
        out2=difflib.get_close_matches(userin, data.keys())
        partmatch(out)
        return "Closest matches to %s: \n" %userin + str(out2)
    else:
        return ("Word not in dictionary\n")
def partmatch (word):
    userin=input ("Did you want to see the meaning for %s \n Yes or No?" %word)
    userin=userin.lower()
    if user == ("yes" or "no" or "y" or "n"):
        return word


userin=input ("Enter a word: \n")
print (extractj(userin.lower()))
