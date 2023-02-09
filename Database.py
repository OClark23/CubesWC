import sqlite3

import secrets
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = connection.cursor()  # ready to read/write data
    return connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
 banner_id INTEGER PRIMARY KEY,
 first_name TEXT NOT NULL,
 last_name TEXT NOT NULL,
 gpa REAL DEFAULT 0,
 credits INTEGER DEFAULT 0
 );''')


def create_entries_tables(cursor: sqlite3.Cursor):
    values_in_the_table = [(1, ' Warren',
                            'Clark',
                            4.0,
                            120
                            ),
                           (2,"Santore",
                            "John",
                            4.7,
                            10000)]
    cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?);", values_in_the_table)


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def my_data():
    con, cursor = open_db("studentDatabase.db")
    setup_db(cursor)
    create_entries_tables(cursor)
    close_db(con)
