from flask_app import app
from flask import render_template, redirect,session, request
from flask_app.models import band

@app.route('/band/new')
def new_band():
    # if "user_id" not in session:
    #     return redirect("/")
    # data = {
    #     "id": id
    # }
    return render_template('newband.html')

@app.route('/band/create', methods=['POST'])
def create_band():
    if not band.Band.validate_newband(request.form):
        return redirect('/band/new')
    if "user_id" not in session:
        return redirect("/")
    # show.Show.save(request.form)
    # return redirect('/dashboard')
    else:
        data = {
            "band_name": request.form["band_name"],
            "music_genre": request.form["music_genre"],
            "home_city": request.form["home_city"],
            "user_id": session["user_id"],
        }
        band.Band.save(data)
        return redirect('/dashboard')

@app.route("/band/<int:id>")
def view_band(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id
    }    
    return render_template("showband.html", band = band.Band.get_oneband(data))


@app.route('/delete/<int:id>')
def delete_band(id):
    band.Band.delete_band(id)
    return redirect ('/dashboard')


@app.route("/band/<int:id>/update", methods=["POST"]) 
def update(id):
    if "user_id" not in session:
        return redirect("/")
    if not band.Band.validate_newband(request.form):
        return redirect(f"/band/{id}/edit")
    else:
        data = {
            "band_name": request.form["band_name"],
            "music_genre": request.form["music_genre"],
            "home_city": request.form["home_city"],
            "id":id
        }
        band.Band.edit_band(data)
        return redirect('/dashboard')

@app.route('/band/<int:id>/edit')
def edit_band(id):
    if "user_id" not in session:
        return redirect("/")
    data = {

            "id":id
        }
    return render_template('editband.html', band = band.Band.get_oneband(data))
