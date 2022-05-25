from flask import render_template, request, redirect, session
from flask_app import app

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dashboard')
def dashboard():
    return render_template ('dashboard.html')

@app.route('/players/create', methods=["POST"])
def create_player():
    print (request.form)
    session['user_name']= request.form['user_name']
    session['user_email']= request.form['user_email']
    # return render_template('user_info.html', user_name=request.form['user_name'], email=request.form['user_email'])
    return redirect('/players/info')

@app.route('/players/info')
def player_info():
    return render_template('user_info.html')  
    # user_name=session['user_name'], email=session['user_email']

@app.route('/players/clear')
def clear_player():
    session.clear()
    return redirect('/players/info')