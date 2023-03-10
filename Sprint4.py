import sqlite3
from tkinter import messagebox
import matplotlib.pyplot as plt
from django.conf.locale import tk

from Sprint3 import add_entry_to_db


def on_submit(db_cursor: sqlite3.Cursor, entry_data: dict, entry_fields: dict):
    add_entry_to_db(db_cursor, entry_data)
    db_cursor.connection.commit()
    messagebox.showinfo("Success", "Entry added to database!")

    # Generate data for the bar chart
    counts = db_cursor.execute("SELECT subject_area, COUNT(*) FROM WuFooData GROUP BY subject_area").fetchall()
    labels = [c[0] for c in counts]
    values = [c[1] for c in counts]

    # Create and show the bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xticklabels(labels, rotation=45)
    ax.set_title("Entries by Subject Area")

    # Add labels to the bars
    for i, v in enumerate(values):
        ax.text(i, v + 0.5, str(v), color='black', ha='center')

    # Show the chart
    plt.show()

    for field in entry_fields.values():
        field.delete(0, tk.END)
