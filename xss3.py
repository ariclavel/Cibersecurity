import webbrowser 
import mechanize
url = "http://localhost:3000/#/search"
attack_no = 1
payload = "otro.txt"
x = open(payload, 'r')

for line in x:
   webbrowser.open(url)
   webbrowser.select_form(nr = 0)
   webbrowser["id"] = line
   res = webbrowser.submit()
content = res.read()

if content.find(line) > 0:
    print("Possible XSS")
