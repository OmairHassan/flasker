from flask import Flask, render_template

# Creates a flask instance
app = Flask(__name__)

@app.route("/")

def index():
	return "<p>A</p>"
	# return render_template(home.html)