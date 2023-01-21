import requests

url = 'https://facebook.com'
url = 'http://testphp.vulnweb.com/userinfo.php'
def check_csrf_vuln(url):

    is_vulnerable=True
    response = requests.request("GET", url)
    resp_header = response.headers
    #"If a web app contains at least one of these headers then it is protected against CSRF"
    searched_headers = ['Access-Control-Allow-Origin','Cross-Origin-Opener-Policy-Report-Only', 'Set-Cookie', 'X-Frame-Options', 'X-Forwarded-Host','Origin','Referer']


    for key in resp_header.keys():
        if key in searched_headers:
            is_vulnerable=False

    return is_vulnerable

#print(check_csrf_vuln(url))
