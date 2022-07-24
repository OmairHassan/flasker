from flask import Flask, render_template

# Creates a flask instance
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])

def login():
	return render_template("login.html")