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

    thread_header = "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, fullText TEXT)"
    create_table("posts",thread_header)

    thread_reply = "(id INTEGER, author TEXT, fulltext TEXT)"
    create_table("replies", thread_reply)

    health_header = "(username TEXT, sleep INTEGER, calories INTEGER, exercise INTEGER, date TEXT)"
    create_table("health_info",health_header)


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

def add_account(username, password):
    if not(account_exists(username)):
        query("INSERT INTO userInfo VALUES (?, ?)", (username, password))
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
    query("INSERT INTO posts (title, author, fullText) VALUES (?, ?, ?)", (title, author, text))

def add_health_info(username, sleep, calories, exercise, date):
    query("INSERT INTO health_info (username, sleep, calories, exercise, date) VALUES (?, ?, ?, ?, ?)", (username, sleep, calories, exercise, date))

def get_user_stories():
    titles = []
    stories = get_table_list("posts")
    for story in stories:
        titles.append(story)
    return titles
