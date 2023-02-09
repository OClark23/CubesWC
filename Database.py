import sqlite3

import secrets
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = connection.cursor()  # ready to read/write data
    return connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS wuffoo(
 title_name INTEGER PRIMARY KEY,
 organization_name TEXT NOT NULL,
 email_name TEXT NOT NULL,
 website_name TEXT NOT NULL,
 phone_number TEXT NOT NULL,
 Oppurtunities_interested REAL DEFAULT,
 name_permission REAL DEFAULT,
 );''')

def create_entries_tables(cursor: sqlite3.Cursor):
    values_in_the_table = [(2, 'Cube project',
                            'Lorem Ipsum',
                            'fbar@org.com',
                            'org.com',
                            '888-123-4567',
                            'none',
                            'yes'
                            ),
                           (3,'Cube project',
                            'differ env',
                            'hackbar@org.com',
                            'org.com',
                            '888-272-1723',
                            'Networking Event,Career Panel,Internships',
                            'yes')]
    cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?,?,?);", values_in_the_table)


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def my_data():
    con, cursor = open_db("studentDatabase.db")
    setup_db(cursor)
    create_entries_tables(cursor)
    close_db(con)
