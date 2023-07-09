# db_migrate.py


import sqlite3
from project import db, app
from project._config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("ALTER TABLE user RENAME TO old_user")

    with app.app_context():
        db.create_all()
    
    c.execute("SELECT username, email, password FROM old_user ORDER BY user_id ASC")

    data = [(row[0], row[1], row[2]) for row in c.fetchall()]

    c.executemany("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", data)

    c.execute("DROP TABLE old_user")