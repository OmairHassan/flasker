from flask import Flask, render_template

# Creates a flask instance
app = Flask(__name__)

@app.route("/")

def index():
	return render_template("index.html")