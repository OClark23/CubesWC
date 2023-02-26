import tkinter.ttk as ttk


def set_style():
    # Create a style object
    style = ttk.Style()

    # Set the theme
    style.theme_use('clam')

    # Set the background color of the entire window
    style.configure('.', background='#f5f5f5')

    # Set the foreground color of all the labels
    style.configure('TLabel', foreground='#333')

    # Set the font and size of all the labels
    style.configure('TLabel', font=('Arial', 12))

    # Set the font and size of all the entry fields
    style.configure('TEntry', font=('Arial', 12))

    # Set the padding for all widgets
    style.configure('.', padding=(10, 10, 10, 10))

    # Set the background color and padding of the submit button
    style.configure('Submit.TButton', background='#4CAF50', padding=(10, 5))

    # Set the foreground color and font of the submit button
    style.configure('Submit.TButton', foreground='#fff', font=('Arial', 12))

    # Set the hover and active background color of the submit button
    style.map('Submit.TButton', background=[('active', '#3e8e41'), ('hover', '#3e8e41')])

