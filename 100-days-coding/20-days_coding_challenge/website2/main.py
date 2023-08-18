from flask import Flask, render_template
from . import index

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if "__name__" == "main":
    app.run()