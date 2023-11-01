from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home"

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        input3 = request.form['input3']
        # Process the data or save it to a database if needed

    return render_template('admin.html')

@app.route('/guest', methods=['GET', 'POST'])
def guest():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']
        input3 = request.form['input3']
        # Process the data or save it to a database if needed

    return render_template('guest.html')

if __name__ == '__main__':
    app.run(debug=True)