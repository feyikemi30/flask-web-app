from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/')
def index():
 return "I am almost a Devops Engineer!"

if __name__ == '__main__':
 app.run(host='0.0.0.0')
