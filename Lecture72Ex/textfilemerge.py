from datetime import datetime

def reader (filename):
    with open (filename) as file1:
        filecontent=file1.read()
        return (filecontent+"\n")

def writer (filename, whatwrite):
    with open (filename, "a+") as file2:
        file2.write(whatwrite)


currenttimeobj=datetime.now()
currenttimestr=currenttimeobj.strftime("%Y-%m-%d-%h-%M-%S-%f")+".txt"
i=1
while i<4:
    contents=reader("file"+ str(i)+".txt")
    i=i+1
    writer(currenttimestr , contents)
