import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

# initialize an HTTP session & set the browser
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
def getForms(url):

    req = bs(requests.get(url).content, "html.parser")
    return req.find_all("form") 
    """arr = []
    for link in bs.find_all("a"):
        lien = link.get("href")
        print(lien)
        
        if(lien[-1] == "l" and lien[-2] == "m" and lien[-3] == "t" and lien[-4] == "h" and lien[-5] == "."):
            arr.append(lien)
        if(lien[-1] == "p" and lien[-2] == "h" and lien[-3] == "p" and lien[-4] == "."):
            arr.append(lien)
    print("ahor next")
    for m in arr:
        print(m)"""

def errors(response):
   
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # if you find one of these errors, return True
        if error in response.content.decode().lower():
            return True
    # no error detected
    return False


def attackSql(url):
    # test on URL
    """for c in "\"'":
        # add quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # make the HTTP request
        res = s.get(new_url)
        if errors(res):
            # SQL Injection detected on the URL itself, 
            # no need to preceed for extracting forms and submitting them
            print("SQL Injection vulnerability detected!!!!!!")
            return
    # test on HTML forms"""
    forms = getForms(url)
    if(len(forms) == 0):
        print("No forms detected")
        return
    print(f"{len(forms)} forms")
    for form in forms:
        form_details = {}
        #We take the attributes action like in the other attack
        try:
            action = form.attrs.get("action").lower()
        except:
            action = None
        # to know if it s post or get and aply it
        method = form.attrs.get("method", "get").lower()
        # get all the input details such as type and name
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})
        # put everything to the resulting dictionary
        form_details["action"] = action
        form_details["method"] = method
        form_details["inputs"] = inputs
      
        for c in "\"'":
            # meke a request with data that we declare here
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    # any input form that is hidden or has some value,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # all others except submit, use some junk data with special character
                    data[input_tag["name"]] = f"test{c}"
            # different request depending on the method
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
            # see if the error exists
            if errors(res):
                print("SQL Injection vulnerability detected!!!!!!")
                print("Form:")
                pprint(form_details)
                break

if __name__ == "__main__":
    url = "http://testphp.vulnweb.com/artists.php?artist=1"
    attackSql(url)