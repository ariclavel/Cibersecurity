import mechanize
browser = mechanize.Browser()
url = "http://localhost/HappyFamily/App/View/Dashboard.php"
attack_no = 1
v = open("otro.txt", 'r')
for line in v:
   browser.open(url)
   browser.select_form(nr = 0)
   browser["id"] = line
   res = browser.submit()
content = res.read()
output = open('response/' + str(attack_no) + '.txt', 'w')
output.write(content)
output.close()
print(attack_no)
attack_no += 1