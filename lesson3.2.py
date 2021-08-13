from random import randint
from flask import Flask

app = Flask(__name__)

@app.route("/get_random")
def random():
    random_num = randint(1,10)
    return {'random' : random_num}, 200

@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_user(user_name= 'no one'):
    return 'Hello ' + user_name, 200

#@app.route("/welcome")
def welcome():
    return "<H1 id='welcome'>Welcome!</H1>", 200

app.run(host='127.0.0.1', debug=True, port=5000)