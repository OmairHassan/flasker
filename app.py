from flask import Flask, render_template, request

# Creates a flask instance
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
	return "<h1>A</h1>"