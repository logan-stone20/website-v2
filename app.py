from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", title = "Home")

@app.route("/projects")
def projects():
	return render_template("projects-grid-cards.html", title = "Projects")

@app.route("/resume")
def resume():
	return render_template("resume.html", title = "Resume")

if __name__ == "__main__":
	app.run()