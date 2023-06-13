import sqlite3
DB_FILE = "data.db"

def query(sql, extra = None):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    if extra is None:
        res = c.execute(sql)
    else:
        res = c.execute(sql, extra)
    db.commit()
    db.close()
    return res

def create_table(name, header):
    query(f"CREATE TABLE IF NOT EXISTS {name} {header}")

def setup():
    users_header = ("(username TEXT, password TEXT)")
    create_table("userInfo", users_header)

    thread_header = "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, fullText TEXT, replies INTEGER)"
    create_table("posts",thread_header)

    thread_reply = "(id INTEGER, author TEXT, fulltext TEXT)"
    create_table("replies", thread_reply)

    health_header = "(date TEXT, sleep INTEGER, calories INTEGER, exercise INTEGER)"
    create_table("health_info",health_header)

    diet_header = "(username TEXT, calories INTEGER, protein INTEGER, carbs INTEGER, fat INTEGER)"
    create_table("diet_info", diet_header)
    
    # physicals_header = ("(age INTEGER, height INTEGER, weight INTEGER, tobacco TEXT, gender TEXT, sex TEXT, pregnant TEXT)")
    # create_table("physcialsInfo", physicals_header)

def get_table_list(tableName):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT * from {tableName}")
    out = res.fetchall()
    db.commit()
    db.close()
    return out

def get_posts_row(id):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute("SELECT * FROM posts WHERE ID = ?", (id,))
    out = res.fetchall()
    db.commit()
    db.close()
    return out

def get_reply_row(id):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute("SELECT * FROM replies WHERE ID = ?", (id,))
    out = res.fetchall()
    db.commit()
    db.close()
    return out

def get_replies():
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute("SELECT * FROM replies")
    out = res.fetchall()
    db.commit()
    db.close()
    return out

def add_reply(id, author, text):
    query("INSERT INTO replies VALUES (?, ?, ?)", (id, author, text))
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("UPDATE posts SET replies = replies + 1 WHERE id = ?", (id,))
    db.commit()
    db.close()

def get_totalnutrition(username, category):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    query = "SELECT {} FROM diet_info WHERE username = ?".format(category)
    c.execute(query, (username,))
    db.commit()
    db.close()

def add_nutrition(username, calories, protein, carbs, fat):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()

    calories_query = "UPDATE diet_info SET calories = calories + {} WHERE username = ?".format(calories)
    c.execute(calories_query, (username,))
    protein_query = "UPDATE diet_info SET protein = protein + {} WHERE username = ?".format(protein)
    c.execute(protein_query, (username,))
    carbs_query = "UPDATE diet_info SET carbs = carbs + {} WHERE username = ?".format(carbs)
    c.execute(carbs_query, (username,))
    fat_query = "UPDATE diet_info SET fat = fat + {} WHERE username = ?".format(fat)
    c.execute(fat_query, (username,))

    db.commit()
    db.close()


def add_account(username, password):
    if not(account_exists(username)):
        query("INSERT INTO userInfo VALUES (?, ?)", (username, password))
        query("INSERT INTO diet_info VALUES (?)", (username,))
    else:
        return -1

#return true if username and password are in db, false if one isn't
def verify_account(username, password):
    accounts = get_table_list("UserInfo")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def account_exists(username):
    accounts = get_table_list("userInfo")
    for account in accounts:
        if account[0] == username:
            return True
    return False

def add_story(title, author, text):
    query("INSERT INTO posts (title, author, fullText, replies) VALUES (?, ?, ?, ?)", (title, author, text, 0))

def add_health_info(date, sleep, calories, exercise):
    query("INSERT INTO health_info (date, sleep, calories, exercise) VALUES (?, ?, ?, ?)", (date, sleep, calories, exercise))

def get_user_stories():
    titles = []
    stories = get_table_list("posts")
    for story in stories:
        titles.append(story)
    return titles
