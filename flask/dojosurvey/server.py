from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "shush"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect ('/success')

@app.route('/result')
def result():
    render_template('success.html')



if __name__=="__main__":
    app.run(debug=True)