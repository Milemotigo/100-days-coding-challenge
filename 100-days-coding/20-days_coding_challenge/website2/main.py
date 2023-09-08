from flask import Flask, render_template, Blueprint, url_for
from index import blue_print

app = Flask(__name__)

app.register_blueprint(blue_print)
if __name__=="__main__":
    app.run(debug=True)
