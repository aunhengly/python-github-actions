import re
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/admin')
def admin():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        input3 = request.form['input3']
        # Process the data or save it to a database if needed

    return render_template('admin.html')

@app.route('/guest')
def guest():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        input3 = request.form['input3']
        # Process the data or save it to a database if needed

    return render_template('guest.html')


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content