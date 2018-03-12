import json

def extractj (key):
    data=json.load(open("data.json"))
    if key in data:
        return (data[key])
    else:
        return ("Word not in dicitionary")

userin=input ("Enter a word: ")
print (extractj(userin.lower()))
