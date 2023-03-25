from flask import Flask, render_template, request

app = Flask(__name__)

<<<<<<< HEAD
app.debug = True

@app.route("/")
def index():
 return "I am almost a Devops Engineer!"

if __name__ == '__main__':
 app.run(host='0.0.0.0')
=======
@app.route("/")
def hello():
 return "I am almost a Devops Engineer!"
>>>>>>> 5aa5d77e2291ad50ff9c8ca8a9fc4edd3cf6d2a1

if __name__ == "__main__":
 app.run(host='0.0.0.0')