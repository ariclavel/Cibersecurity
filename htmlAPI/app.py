
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)
import xssAttack.py
#rendering the HTML page which has the button
@app.route('/')
def json():
    return render_template('main.html')

@app.route("/forward/", methods=['POST','GET'])
def move_forward():
    if request.method == "GET":
        forward_message = "Moving Forward..."
        return render_template('info.html', titulo=forward_message)

    #Moving forward code
    if request.method == "POST":
        req = request.form
        print(req)
        a = req.get("lien")
        print(a)
        url = "http://testphp.vulnweb.com/artists.php?artist=1"
        b = xssAttack.attackSql(a)
        return render_template("main.html", titulo=b)
 
    