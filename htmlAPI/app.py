
from flask import Flask, render_template, Response, request, redirect, url_for, send_file

app = Flask(__name__)
# importing the attacks
from attack_modules.xss.xssAttack import detectXSS as xss_attack
from attack_modules.xss.xss2 import attack as xss2_attack
from attack_modules.xss.xss3 import attack as xss3_attack

from attack_modules.xxe.xxe import upload_file as xxe_attack

from attack_modules.sql_injection.sqlInjection import attackSql as sql_attack

from attack_modules.csrf.check_csrf import check_csrf_vuln as csrf_attack

from attack_modules.crlf.check_crlf import check_crlf_vuln as crlf_attack

from attack_modules.dos.dosAtack import dos_attack as execute_dos_attack

from attack_modules.brute_force.bruteForce import bruteForceAttack as brute_force_attack

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
        # initializing the test dictionary
        attack_report = {
                "url": req.get("lien"),
                "xss1":False,
                "xss2":False,
                "xss3":False,
                "xxe":False,
                "sql":False,
                "csrf":False,
                "crlf":False,
                }
        # making the link work for the HTTP requests
        url = "http://" + req.get("lien")

        # testing for all the implemented attacks
        try:
            attack_report["xxe"]  =  xxe_attack(url)
        except:
            pass
        try:
            attack_report["xss1"] =  xss_attack(url)
        except:
            pass
        try:
            attack_report["xss2"] =  xss2_attack(url)
        except:
            pass
        try:
            attack_report["xss3"] =  xss3_attack(url)
        except:
            pass
        try:
            attack_report["sql"]  =  sql_attack(url)
        except:
            pass
        try:
            attack_report["csrf"] =  csrf_attack(url)
        except:
            pass
        try:
            attack_report["crlf"] =  crlf_attack(url)
        except:
            pass

        return render_template("main.html", attack_report = attack_report)

@app.route("/info/", methods=['GET'])
def info():
    return render_template("info.html")
@app.route("/info-sec/", methods=['GET'])
def infoSec():
    return render_template("info-sec.html")
@app.route("/contact/", methods=['GET'])
def infoSec():
    return render_template("contact.html")
@app.route("/tools/", methods=['GET'])
def infoSec():
    return render_template("tools.html")

#background process happening without any refreshing
@app.route('/dos')
def dos_attack():
    is_vulnable, message = execute_dos_attack(request.args.get("url"))
    return ({"is_vulnable": is_vulnable, "message": message})

@app.route("/bruteForce", methods=['POST'])
def brute_force():
    req = request.form
    attack_report = {
        "vulnareble": req.get("login_url"),
        "message":False,
    }
    attack_report["vulnareble"], attack_report["message"] = brute_force_attack(req.get("login_url"), req.get("username"), req.get("error"))
    return render_template("bruteForceReport.html", attack_report = attack_report)
