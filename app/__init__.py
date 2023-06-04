from flask import Flask, render_template, request, session, redirect, url_for
import os
import db_tools

app = Flask(__name__)
app.secret_key = os.urandom(32)

db_tools.setup()

@app.route('/')
def index():
    if 'username' in session:
        return render_template("home_page.html")
    return render_template('login.html') 

@app.route('/login', methods = ['GET','POST'])
def login():
    #Check if it already exists in database and render home page if it does
    #otherwise redirect to error page which will have a button linking to the login page
    username = request.form.get('username')
    password = request.form.get('password')
    if db_tools.verify_account(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/home")
    if request.form.get('submit_button') is not None:
        return render_template("create_account.html")
    else:
        return render_template('error.html',msg = "username or password is not correct")

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db_tools.add_account(userIn, passIn) == -1:
            return f"account with username {userIn} already exists"
        else:
            return render_template("login.html")
    return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("Register.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    if db_tools.verify_account(username, password):
        return render_template("home_page.html")

def verify_session():
    if 'username' in session and 'password' in session:
        if db_tools.verify_account(session['username'], session['password']):
            return True
    return False

@app.route("/physical_data")
def physcials():
    return render_template("Physcial.html")

@app.route("/survey_redirect")
def surveyredirect():
    return render_template("survey.html")

if __name__ == '__main__':
    app.debug = True
    app.run()