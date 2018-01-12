import os
from flask import Flask,render_template, request,json, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/user/<user>')
def show_user_profile(user):
    return 'User %s' % user

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return hi(user)
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hi(name = None):
    return render_template('hello.html', name=name)

# @app.route('/signUp')
# def signUp():
#     return render_template('signUp.html')
#
# @app.route('/signUpUser', methods=['POST'])
# def signUpUser():
#     user =  request.form['username'];
#     password = request.form['password'];
#     return json.dumps({'status':'OK','user':user,'pass':password});

if __name__=="__main__":
    app.run()
