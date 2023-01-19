from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/')
def json():
    return render_template('main.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('main.html', forward_message=forward_message);