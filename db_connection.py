import sqlite3

def add():
    con=sqlite3.connect(database=r'drugs.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Medicine(PROD_ID text PRIMARY KEY, COMPANY_NAME text, TYPE_OF_MED text, MED_NAME text, PRICE text, QUANTITY text)")
    con.commit()
	



    con==sqlite3.connect(database=r'Users.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Users(user text PRIMARY KEY, password text)")
    con.commit()


add()