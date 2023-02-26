import pytest
import tkinter as tk
import sqlite3
from unittest.mock import MagicMock, patch
from gui import SQLiteBrowserGUI

__all__ = ['SQLiteBrowserGUI']


@pytest.fixture
def gui():
    return SQLiteBrowserGUI('DatabaseStuff.db')


def test_gui_display_entries(gui, capsys):
    gui.root.update()
    assert gui.root.winfo_exists() == 1

    entries = gui.get_entries()
    assert len(entries) > 0

    listbox = gui.root.children['!listbox']
    assert listbox.size() == len(entries)

    text = gui.root.children['!text']
    for i in range(len(entries)):
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(i)
        listbox.event_generate('<<ListboxSelect>>')
        captured = capsys.readouterr()
        assert entries[i][1] in captured.out
        assert entries[i][2] in captured.out
