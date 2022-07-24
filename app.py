from flask import Flask, render_template, request

# Creates a flask instance
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])

def login():
	if request.method == "POST":
		password=request.form["password"]
		if password == "a":
			return render_template("index.html")
	return render_template("login.html")