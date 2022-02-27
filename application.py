from flask import Flask, request, Response, redirect, url_for, render_template, jsonify
import praw

application = Flask(__name__)

@application.route('/')
def index():
	users = customers()
	for i in users:
		print(i[0])
	return render_template('app.html', products = users)

if __name__ == '__main__':
	application.run(debug=True)