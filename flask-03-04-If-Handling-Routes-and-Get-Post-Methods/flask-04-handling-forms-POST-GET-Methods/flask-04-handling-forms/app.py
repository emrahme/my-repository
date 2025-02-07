# Import Flask modules
from flask import Flask, render_template, redirect, request, url_for


# Create an object named app
app = Flask(__name__)

# Create welcome page with main.html file and assign it to the root path
@app.route("/")
def welcome():
    return render_template("main.html", name= "Erin")

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised
@app.route("/greet")
def greet():

    if "user" in request.args:
        the_user = request.args.get("user")
        return render_template("greet.html", user=the_user)
    else:
        return "<Missing user in query string>"
    


# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')
@app.route("/login", methods= ["GET", "POST"])
def login():

    if request.method == "POST":    # the POST Method
        user_name = request.form.get("username")
        pw = request.form.get("password")
        if user_name == "erin" and pw == "erin":        #we pretend it is the correct username and password
            return render_template("secure.html", user=user_name)
        else:
            return render_template("login.html", control=1, user=user_name)

    
    else:
        return render_template("login.html")
# Add a statement to run the Flask application
if __name__ == "__main__":
    app.run(debug=True)