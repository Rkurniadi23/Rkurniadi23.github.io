from flask import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def resume():
	return render_template('index.html')

@app.route("/background")
def background():
	return render_template('background.html')

@app.route("/projects", methods= ['GET', 'POST'])
def projects():
	return render_template('projects.html')

@app.route("/work")
def work():
	return render_template('work.html')


if __name__ == "__main__":
    app.run(debug=True)