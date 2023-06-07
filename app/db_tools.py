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
    thread_header = "(title TEXT, fullText TEXT)"
    create_table("posts",thread_header)
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

def add_story(title, text):
    query("INSERT INTO posts VALUES (?, ?)", (title, text))

def get_user_stories():
    comments = []
    stories = get_table_list("posts")
    for story in stories:
        comments.append(story[1])
    return comments