import sqlite3

import secrets
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = connection.cursor()  # ready to read/write data
    return connection, cursor


def create_entries_tables(cursor: sqlite3.Cursor, table_name):
    cursor.execute("INSERT INTO ENTRIES VALUES: 'Name:  Warren Clark' 'Title: Automate this form' 'Organization: BSU' 'Email: WarrenClark306@gmail.com' 'Opportunities Interested in:'")



def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


