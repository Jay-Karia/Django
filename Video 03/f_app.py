from flask import Flask, render_template
from flask.templating import render_template_string

f_app = Flask(__name__)
@f_app.route("/")
def home():
    name = "Jay"
    return render_template("index.html", name=name)

@f_app.route("/about")
def about():
    name = 'mahil'
    return render_template("about.html", name2=name)

f_app.run(debug=True)
