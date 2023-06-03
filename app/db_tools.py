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
