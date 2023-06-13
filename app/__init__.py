from flask import Flask, render_template, request, session, redirect, url_for
import os
import db_tools
import api
from datetime import datetime
from datetime import date

app = Flask(__name__)
app.secret_key = b'\xed|@\x89\xbf\xb1<\x06\x81\xf4R\x8b!\xad\xe7T\x11Gb\x8c\xc9x3(vsN\xa0\xfb\xef\xc9\x9e'

db_tools.setup()

@app.route('/')
def index():
    if 'username' in session:
        health_contents = db_tools.get_table_list("health_info")
        return render_template("home_page.html",health_contents = health_contents)
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
    return render_template("register.html")

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
        health_contents = db_tools.get_table_list("health_info")
        return render_template("home_page.html",health_contents = health_contents)

def verify_session():
    if 'username' in session and 'password' in session:
        if db_tools.verify_account(session['username'], session['password']):
            return True
    return False

@app.route("/physical_data")
def physcials():
    return render_template("physical.html")

@app.route("/physical",methods=['POST'])
def physical_form():
    age = request.form.get("age")
    gender = request.form.get("gender")
    pregnant = request.form.get("pregnant")
    tobacco = request.form.get("tobacco")
    sex = request.form.get("sex")
    des, x = api.get_reccomendations(age, gender, pregnant, tobacco, sex)
    return render_template("reccomendations.html",descript = des, recs=x)

@app.route("/survey_redirect")
def surveyredirect():
    return render_template("survey.html")

@app.route("/health",methods=['POST'])
def health_form():
    calories = request.form.get("calories")
    

    sleeps = request.form.get("sleeps")
    wakes = request.form.get("wakes")

    exercise = request.form.get("excercises")
    
    #date_td = str(date.today())
    date_td = request.form.get("date")
    #print(date_td)

    # Convert the strings to datetime objects
    start_time = datetime.strptime(sleeps, '%Y-%m-%dT%H:%M')
    end_time = datetime.strptime(wakes, '%Y-%m-%dT%H:%M')

    # Calculate the timedelta between the two datetime values
    time_difference = end_time - start_time

    # Calculate the number of minutes elapsed
    sleep_minutes = time_difference.total_seconds() / 60
    
    # db_tools.add_health_info(date_td, sleep_minutes, calories, exercise)
    health_contents = db_tools.get_table_list("health_info")
    print(health_contents)
    return render_template("home_page.html",health_contents = health_contents)

@app.route("/diary", methods=['GET','POST'])
def diary():
    username = session['username']
    input_text = ""
    if request.method == 'POST':
        input_text = request.form["foodName"]
        print(input_text)
    food_contents = api.get_nutrition(input_text)
    print(food_contents)
    print(type(food_contents))

    # food_calories = food_contents[0]["calories"]
    # food_protein = food_contents[0]["protein_g"]
    # food_carbs = food_contents[0]["carbohydrates_total_g"]
    # food_fat = food_contents[0]["fat_total_g"]

    # db_tools.add_nutrition(username, food_calories, food_protein, food_carbs, food_fat)
    # total_calories = db_tools.get_totalnutrition(username, "calories")
    # total_protein = db_tools.get_totalnutrition(username, "protein")
    # total_carbs = db_tools.get_totalnutrition(username, "carbs")
    # total_fat = db_tools.get_totalnutrition(username, "fat")

    # return render_template('diary.html', total_calories=total_calories, total_protein=total_protein, total_carbs=total_carbs, total_fat=total_fat)
    return render_template('diary.html')
    

@app.route("/forum", methods=['GET','POST'])
def forum():
    forumreplies = len(db_tools.get_replies())
    if 'username' not in session:
        return redirect("/login")
    if request.method == 'POST':
        title = request.form['posttitle']
        text = request.form['posttext']
        db_tools.add_story(title, session.get('username'), text)
        user_inputs = db_tools.get_user_stories()
        return render_template("forum.html",arr=user_inputs, numbposts = len(user_inputs), numbreplies = forumreplies, account = session.get('username'))
    else:
        user_inputs = db_tools.get_user_stories()
        print(user_inputs)
        return render_template("forum.html",arr=user_inputs, numbposts = len(user_inputs), numbreplies = forumreplies, account = session.get('username'))
    
@app.route("/forum/<id>", methods=['GET','POST'])
def fpost(id):
    if 'username' not in session:
        return redirect("/login")
    if request.method == 'POST':
        text = request.form['posttext']
        info = db_tools.get_posts_row(id)
        db_tools.add_reply(id, session.get('username'), text)
        replies = db_tools.get_reply_row(id)
        return render_template("forumpost.html", arr = info, replies = replies, id = id, account = session.get('username'))
    else:
        info = db_tools.get_posts_row(id)
        user_inputs = db_tools.get_user_stories()
        replies = db_tools.get_reply_row(id)
        return render_template("forumpost.html", arr = info, numbposts = len(user_inputs), replies = replies, id = id, account = session.get('username'))


if __name__ == '__main__':
    app.debug = True
    app.run() 