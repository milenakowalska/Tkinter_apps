import tkinter as tk
import sqlite3, os
from my_classes import Myroot, Mytoplevel, MyButton, Word

def show():
    top_show = Mytoplevel()
    top_show.geometry('600x640')

    delet_entry = tk.Entry(top_show.frame, width = 30, bg = '#9999FF')
    delet_entry.pack()

    delet_label = tk.Label(top_show.frame, text = 'Delete a word with ID number: ', bg = '#9999FF')
    delet_label.pack()

    tk.Button(top_show.frame, text = 'Delete a word', highlightbackground = 'black', highlightthickness=6, fg = 'black', command = lambda: delete_word(delet_entry.get())).pack() 

    yscrollbar = tk.Scrollbar(top_show.frame, orient="vertical")
    yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas3 = tk.Canvas(top_show.frame, yscrollcommand=yscrollbar.set, bg = '#9999FF', bd = 0, highlightthickness = 0, height = 260, width = 550)
    canvas3.pack(side=tk.LEFT, fill=tk.BOTH)
    yscrollbar.config(command=canvas3.yview)

    connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "de2fr2.db"))
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM words")
    records = cursor.fetchall()

    print_rec = str('')

    ind = 0

    inner_frame = tk.Frame(canvas3, width=600, height=(len(records)*40), bg = '#9999FF', bd = 0, highlightthickness = 0)
    canvas3.create_window((0,0), window=inner_frame, anchor='nw')

    for items in records:
        print_rec += str(items[3]) + '\t' + str(items[0]) + ' ---> ' + str(items[1]) +  '\n'
        tk.Label(inner_frame, text = print_rec, bg = '#9999FF').grid(row = ind+ 2, sticky = tk.W)
        ind += 1
        print_rec = str('')

    canvas3.configure(scrollregion=canvas3.bbox("all"))

    connection.commit()
    connection.close()

def delete_word(delet_entry):
    
    connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "de2fr2.db"))
    cursor = connection.cursor()
    cursor.execute('DELETE from words WHERE oid= ' + delet_entry)      
    connection.commit()
    connection.close() 