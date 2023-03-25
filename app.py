from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
 return "I am almost a Devops Engineer!"
if __name__ == "__main__":
 app.run(host='0.0.0.0')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

