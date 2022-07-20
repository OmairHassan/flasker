from flask import Flask, render_template

# Creates a flask instance
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
	return render_template(home.html)