import pytest
import sqlite3
import tkinter as tk

from Sprint3Styled import set_style, create_entry_gui, create_entries_table, add_entry_to_db, on_submit


@pytest.fixture(scope='module')
def test_db_connection():
    db_connection = sqlite3.connect("test.db")
    cursor = db_connection.cursor()
    create_entries_table(cursor)
    yield cursor
    cursor.execute('DROP TABLE IF EXISTS WuFooData;')
    db_connection.close()


@pytest.fixture(scope='module')
def test_gui():
    db_connection = sqlite3.connect(":memory:")
    db_cursor = db_connection.cursor()
    create_entries_table(db_cursor)
    root = tk.Tk()
    create_entry_gui(db_cursor, root)
    yield root, db_cursor
    root.destroy()
    db_connection.close()


def test_create_entries_table(test_db_connection):
    table_info = test_db_connection.execute("PRAGMA table_info('WuFooData')").fetchall()
    assert len(table_info) == 20


def test_add_entry_to_db(test_db_connection):
    entry_data = {
        "prefix": "Dr.",
        "first_name": "Test",
        "last_name": "User",
        "subject_area": "Test",
        "course_project": True
    }
    add_entry_to_db(test_db_connection, entry_data)
    result = test_db_connection.execute("SELECT * FROM WuFooData").fetchall()
    assert len(result) == 1


def test_on_submit(test_gui):
    root, db_cursor = test_gui
    entry_fields = {
        "prefix": tk.StringVar(value="Mr."),
        "first_name": tk.Entry(root),
        "last_name": tk.Entry(root),
        "subject_area": tk.Entry(root),
        "course_project": tk.BooleanVar(value=True)
    }
    entry_data = {
        "prefix": entry_fields["prefix"].get(),
        "first_name": entry_fields["first_name"].get(),
        "last_name": entry_fields["last_name"].get(),
        "subject_area": entry_fields["subject_area"].get(),
        "course_project": entry_fields["course_project"].get()
    }
    on_submit(db_cursor, entry_data, entry_fields)
    result = db_cursor.execute("SELECT * FROM WuFooData").fetchall()
    assert len(result) == 1
    assert result[0][1:] == (
    'Mr.', '', '', '', '', '', '', '', True, False, False, False, False, False, False, 'Test', '', False, '', '')

