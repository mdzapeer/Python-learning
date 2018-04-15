import time
from datetime import datetime as dt

filepath=r"Q:\GOOGLE DRIVE\_Programming\GitHub\Python-learning\App3 Website blocker\simulated_host_path\hosts"
redirect="127.0.0.0"
block_sites=['www.facebook', 'facebook.com', 'www.youtube.com','youtube.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
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
    time.sleep(5)
