#Lets create a simple flask app
# only get method and hello world app
#lets import flask but you need to install flask by "pip install flask"
from flask import Flask
#Now Lets create app
app = Flask(__name__)
#Lets create our first route
@app.route('/')
#Now I will create a function
def hello():
    return "Hello World"

#lets run our app in debug mode and port will be 8080
app.run(debug=True, port=8080)
#lets run over app in terminal and check in browser