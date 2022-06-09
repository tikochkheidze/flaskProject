from flask import Flask, render_template, redirect, url_for, request,session
from datetime import timedelta
app = Flask(__name__,template_folder='template')
app.secret_key = 'bukaka'
app.permanent_session_lifetime = timedelta(seconds=40)

@app.route('/login', methods =['POST','GET'])


def login():

    if request.method == 'post':
        user = request.form['username']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user ' in session:
            return redirect(url_for('user'))

    return render_template('login.html')

@app.route('/registration', methods =['GET', 'POST'])

def registration():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
    return render_template('registration.html')






