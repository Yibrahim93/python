from flask_app import app
from flask import render_template, redirect,session, request
from flask_app.models import show

@app.route('/show/new')
def new_show():
    return render_template('newshow.html')

@app.route('/show/create', methods=['POST'])
def create_show():
    if not show.Show.validate_newshow(request.form):
        return redirect('/show/new')
    # show.Show.save(request.form)
    # return redirect('/dashboard')
    else:
        data = {
            "title": request.form["title"],
            "network": request.form["network"],
            "release_date": request.form["release_date"],
            "description": request.form["description"],
            "user_id": session["user_id"],
        }
        show.Show.save(data)
        return redirect('/dashboard')

@app.route("/show/<int:id>")
def view_show(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": id
    }    
    return render_template("showshow.html", show = show.Show.get_oneshow(data))


@app.route('/delete/<int:id>')
def delete_show(id):
    show.Show.delete_show(id)
    return redirect ('/dashboard')


@app.route("/show/<int:id>/update", methods=["POST"]) 
def update(id):
    if "user_id" not in session:
        return redirect("/")
    if not show.Show.validate_newshow(request.form):
        return redirect(f"/show/{id}/edit")
    else:
        data = {
            "title": request.form["title"],
            "network": request.form["network"],
            "release_date": request.form["release_date"],
            "description": request.form["description"],
            "id":id
        }
        show.Show.edit_show(data)
        return redirect('/dashboard')

@app.route('/show/<int:id>/edit')
def edit_show(id):
    if "user_id" not in session:
        return redirect("/")
    data = {

            "id":id
        }
    return render_template('editshow.html', show = show.Show.get_oneshow(data))
