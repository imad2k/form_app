import sqlite3


def schema(dbpath):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        
    SQL = """DROP TABLE IF EXISTS form;"""
    cursor.execute(SQL)
    
    SQL = """CREATE TABLE form(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR (100),
        phone INTEGER(10),
        password VARCHAR(100)
    );"""
    cursor.execute(SQL)
    
if __name__ == "__main__":
    schema("form.db")
    

