import webbrowser
import mechanize
url = "http://localhost:3000/#/search"

def attack(url):
    attack_no = 1
    #payload = "otro.txt" -- if you run the script from the same folder
    payload = 'attack_resources/otro.txt'
    x = open(payload, 'r')

    for line in x:
       webbrowser.open(url)
       webbrowser.select_form(nr = 0)
       webbrowser["id"] = line
       res = webbrowser.submit()
    content = res.read()

    # then app is vulnerable
    if content.find(line) > 0:
        return True
    else:
        return False
