from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/harry")
def harry():
    return "Hellor harry bhai!"

app.run(debug=True)