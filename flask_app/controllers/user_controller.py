from crypt import methods

from flask_app import app
from flask import render_template,request, redirect
# import the class from friend.py
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.all_users()
    return render_template("Read_all.html", all_users = users)

@app.route("/create")
def render_create():
    return render_template("Create.html")

@app.route("/create_user", methods = ['POST'])
def create_user():
    data = {
        "first_name" :request.form["fname"],
        "last_name" :request.form["lname"],
        "email" :request.form["email"]
    }
    newUser = User.addNew(data)
    #Logic to both create a dictionary from the post data
    # And pass that dictionary to your class method that will insert a user
    return redirect("/create.html")

@app.route("/<int:user_id>")
def show_user(user_id):
    data={
        "id" : user_id
    }
    user = User.show_user(data)
    return render_template("show_user.html", user = user)

@app.route("/users/<int:id>/edit")
def edit(id):
    data ={
        "id" : id
    }
    user = User.show_user(data)
    return render_template("edit.html", user = user)

@app.route("/update_user/<int:id>", methods = ["POST"])
def update_user(id):
    data = {
        "id" : id,
        "first_name" :request.form["fname"],
        "last_name" :request.form["lname"],
        "email" :request.form["email"]
    }
    User.update_user(data)
    return redirect(f"/{id}")


@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')
