from flask_app import app
from flask import render_template, redirect,session, request
from flask_app.models import car

@app.route('/car/new')
def new_car():
    return render_template('newcar.html')

@app.route('/car/create', methods=['POST'])
def create_car():
    if not car.Car.validate_newcar(request.form):
        return redirect('/car/new')
    # car.Car.save(request.form)
    # return redirect('/dashboard')
    else:
        data = {
            "price": request.form["price"],
            "model": request.form["model"],
            "make": request.form["make"],
            "year": request.form["year"],
            "description": request.form["description"],
            "user_id": session["user_id"],
        }
        car.Car.save(data)
        return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete_car(id):
    car.Car.delete_car(id)
    return redirect ('/dashboard')

@app.route('/edit/<int:id>')
def edit_car(id):
    car.Car.edit_car(id)
    return redirect ('/dashboard')