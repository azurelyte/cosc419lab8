from flask import Flask, render_template, Markup, request, session, redirect, abort
MyApp = Flask(__name__)
MyApp.secret_key = "MyNameIsJeff";
import random


@MyApp.route("/")
def index():
        if session.get('login') == "admin":
                return render_template('secret.html',data=Markup("Success"))
        else:
                return redirect("/login")

@MyApp.route("/login")
def login():
        return render_template("login.html")

@MyApp.route("/loginpost", methods=['POST'])
def loginpost():
        if (str(request.form['username']) == "admin" and str(request.form['password']) == "password" ):
                session['login'] = "admin"
                return redirect('/')
                #return render_template('echo.html',data=Markup("Success"))
        else:
                return abort(418)
                #return render_template('echo.html',data=Markup("Fail!"))

@MyApp.errorhandler(418)
def teapot(e):
        return render_template("418_page.html"), 418

@MyApp.route("/logout")
def logout():
        session.pop('login', None)
        return redirect('/')


@MyApp.route("/bulldog")
def bullDog():
        return render_template("child1.html")

@MyApp.route("/german")
def germanDog():
        return render_template("child2.html")

@MyApp.route("/beagle")
def beagleDog():
        return render_template("child3.html")

@MyApp.route("/boxer")
def boxerDog():
        return render_template("child4.html")

@MyApp.route("/pug")
def pugDog():
        return render_template("child5.html")

if __name__ == "__main__":
        MyApp.run()
