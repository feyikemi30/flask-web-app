from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
   return "I am almost a Devops Engineer!"

if __name__ == '__main__':
<<<<<<< HEAD
 
port = int(os.environ.get("PORT", 5000))
   app.run(debug=True, host='0.0.0.0', port=port)

=======

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)
 
>>>>>>> 8897e20924f3aa72cd98dc29452f4ba64b565b46
