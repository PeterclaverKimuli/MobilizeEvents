import requests
from flask import Flask, render_template, url_for, request, jsonify, redirect
from jsondata import ImportJson

app = Flask(__name__)


posts = ImportJson()

@app.route("/")
def home(): 

	return render_template("home.html", posts=posts.posts)

@app.route("/map")
def map():
	return render_template("map.html", title='Map of Events', posts=posts.posts)


if __name__ == '__main__':
	app.run(debug=True)