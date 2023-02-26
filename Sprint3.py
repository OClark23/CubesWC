import tkinter as tk
from tkinter import messagebox
import sqlite3
from typing import Tuple, Dict, Union
from functools import partial

from Sprint3Styled import set_style


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS WuFooData(
    entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    org TEXT,
    email TEXT,
    website TEXT,
    course_project BOOLEAN,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    job_shadow BOOLEAN,
    internship BOOLEAN,
    career_panel BOOLEAN,
    networking_event BOOLEAN,
    subject_area TEXT NOT NULL,
    description TEXT,
    funding BOOLEAN,
    created_date TEXT,
    created_by TEXT);"""
    cursor.execute(create_statement)


def add_entry_to_db(db_cursor: sqlite3.Cursor, entry_data: Dict[str, Union[str, bool]]):
    entry_values = list(entry_data.values())

    # Check if the entryID field is not empty
    if entry_values[0]:
        entry_values[0] = int(entry_values[0])
    else:
        # Set a default value if entryID is empty
        entry_values[0] = None

    db_cursor.execute("""
        INSERT INTO entries (entryID, prefix, first_name, last_name, title, org, email, website, course_project,
        guest_speaker, site_visit, job_shadow, internship, career_panel, networking_event, subject_area, description,
        funding, created_date, created_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, entry_values)


def on_submit(db_cursor: sqlite3.Cursor, entry_data: dict, entry_fields: dict):
    add_entry_to_db(db_cursor, entry_data)
    db_cursor.connection.commit()
    messagebox.showinfo("Success", "Entry added to database!")
    for field in entry_fields.values():
        field.delete(0, tk.END)


def create_entry_gui(db_cursor: sqlite3.Cursor, root: tk.Tk):
    entry_fields = {}
    for i, field in enumerate(["entryID", "prefix", "first_name", "last_name", "title", "org", "email", "website",
                               "course_project", "guest_speaker", "site_visit", "job_shadow", "internship",
                               "career_panel", "networking_event", "subject_area", "description", "funding",
                               "created_date", "created_by"]):
        tk.Label(root, text=field).grid(row=i, column=0)

        # Add a drop-down component for the "prefix" field
        if field == "prefix":
            prefix_choices = ["Mr.", "Mrs.", "Ms.", "Dr."]
            entry_fields[field] = tk.StringVar(value=prefix_choices[0])
            prefix_dropdown = tk.OptionMenu(root, entry_fields[field], *prefix_choices)
            prefix_dropdown.grid(row=i, column=1)
        elif field in ["course_project", "guest_speaker", "site_visit", "job_shadow", "internship", "career_panel",
                       "networking_event"]:
            entry_fields[field] = tk.BooleanVar(value=False)
            tk.Checkbutton(root, variable=entry_fields[field]).grid(row=i, column=1)
        else:
            entry_fields[field] = tk.Entry(root)
            entry_fields[field].grid(row=i, column=1)

    entry_data = {}
    for field, entry in entry_fields.items():
        if field in ["course_project", "guest_speaker", "site_visit", "job_shadow", "internship", "career_panel",
                     "networking_event"]:
            entry_data[field] = entry.get()
        else:
            entry_data[field] = ""

    partial_on_submit = partial(on_submit, db_cursor, entry_data, entry_fields)
    submit_button = tk.Button(root, text="Submit", command=partial_on_submit)
    submit_button.grid(row=len(entry_fields), column=0, columnspan=2)



if __name__ == "__main__":
    db_connection, db_cursor = open_db("test.db")
    create_entries_table(db_cursor)
    # Set the style
    set_style()
    root = tk.Tk()
    create_entry_gui(db_cursor, root)
    root.mainloop()

    close_db(db_connection)
