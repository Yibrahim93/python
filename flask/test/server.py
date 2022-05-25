from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)  

sal = {
        'id': 1,
        'first_name': 'Sal',
        'last_name': 'Nast',
        'email': 'sn@gmail.com',
        'stacks': ['python','p&a']

}

bob = {
        'id': 2,
        'first_name': 'Bob',
        'last_name': 'Gast',
        'email': 'bbg@gmail.com',
        'stacks': ['Java','CSS']

}

alice = {
        'id': 3,
        'first_name': 'Ally',
        'last_name': 'Dast',
        'email': 'aad@gmail.com',
        'stacks': ['MERN','ruby']

}

instructors= [sal, bob, alice]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dashboard')
def dashboard():
    user_data = {
        'first_name': 'Yas',
        'last_name': 'Ibrahim',
        'age': 29,
    }
    my_posts = ['first','second','third']
    return render_template ("dashboard.html", username=user_data, posts=my_posts,instructors=instructors)

@app.route('/users/<int:id>')
def user(id):
    return render_template("user.html", user = instructors[id-1])
if __name__=="__main__":   
    app.run(debug=True)   

