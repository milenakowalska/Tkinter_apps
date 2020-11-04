
import tkinter as tk
import sqlite3, os
from my_classes import Myroot, Mytoplevel, MyButton, Word


def submit(german, french, definition):

    connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "de2fr2.db"))
    c = connection.cursor()
    c.execute("INSERT INTO words VALUES(:german, :french, :definition)", 
        {
                'german' : german.get(),
                'french' : french.get(),
                'definition' : definition.get()
        })
    connection.commit()
    connection.close()

    german.delete(0,tk.END)
    french.delete(0,tk.END)
    definition.delete(0,tk.END)

def add():

    top_add = Mytoplevel()
    top_add.geometry('600x440')

    german = tk.Entry(top_add.frame, width = 30, bg = '#9999FF')
    german.grid(row = 0, column = 1)
    french = tk.Entry(top_add.frame, width = 30, bg = '#9999FF')
    french.grid(row = 1, column = 1)
    definition = tk.Entry(top_add.frame, width = 30, bg = '#9999FF')
    definition.grid(row = 2, column = 1)

    number = 0
    for element in ('German','French','Definition'):
        tk.Label(top_add.frame, text = str(element), bg = '#9999FF').grid(row = number, column = 0)
        number +=1

    submit_button = tk.Button(top_add.frame, text = 'Add a new word!', highlightbackground = '#FF6633',highlightthickness=6, command =lambda: submit(german, french, definition))
    submit_button.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 113)
