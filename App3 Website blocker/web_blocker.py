import time
from datetime import datetime as dt

filepath=r"Q:\GOOGLE DRIVE\_Programming\GitHub\Python-learning\App3 Website blocker\simulated_host_path\hosts"
redirect="127.0.0.0"
block_sites=['www.facebook', 'facebook.com', 'www.youtube.com','youtube.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
            print("inside")
            with open(filepath,'r+') as file:
                content=file.read()
                for website in block_sites:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+' '+website+'\n')
    else:
            print("outside")
            with open(filepath,'r') as file:
                content=file.read()
                file.seek(0)
                for line in file:
                    if any(site in line for site in block_sites) == True:
                        print('found: '+line)
                        content=content.replace(line,"")
                    else:
                        print('not there')
            with open(filepath,'w') as outputfile:
                outputfile.write(str(content))
    time.sleep(5)
