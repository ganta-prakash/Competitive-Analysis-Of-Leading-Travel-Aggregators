from flask import Flask, render_template, request


travel = Flask(_name_) # initializng the flask app


@travel.route('/')
def helloworld():
    return render_template("index.html")

if _name_ == '_main_':
    travel.run(debug = False, port = 5000)