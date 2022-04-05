from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask'

@app.route('/cv')
def show_cv():
    return render_template("index.html")