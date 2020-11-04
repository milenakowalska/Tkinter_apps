
import tkinter as tk
import sqlite3, os, random
from my_classes import Myroot, Mytoplevel, MyButton, Word


def start(): 
    top_start = Mytoplevel()
    top_start.geometry('1000x590')

    ### Choose the random element from dictionary file

    connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "de2fr2.db"))
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM words")
    records = cursor.fetchall()
    connection.commit()
    connection.close()

    newword = Word(random.choice(list(records)))
    ###
    word = tk.Label(top_start.frame, text = newword.german, font = ('Verdana', 40), bg = '#9999FF', fg = 'black' )
    word.grid(row = 1)

    tk.Label(top_start.frame, text = 'Write the word in French', font = ('Verdana', 15), bg = '#9999FF' ).grid(row=2, pady = 10)

    entry_answer = tk.Entry(top_start.frame, bg = '#9999FF')
    entry_answer.grid(row = 3)

    label_solution = tk.Label(top_start.frame, text = '', bg = '#9999FF')
    label_solution.grid(row=5, pady = 10) 

    def check(newword, label_solution, entry_answer):
        tk.Label(top_start.frame, text = ' ', bg = '#9999FF', padx=200).grid(row=5, pady = 10, ipadx=40)
        answer = str(entry_answer.get())

        if str(newword.french) == answer:
            label_solution =  tk.Label(top_start.frame, text = 'CORRECT!', font = ('Verdana', 15), bg = '#9999FF' , fg = '#006600')
        else:
            label_solution = tk.Label(top_start.frame, text = 'WRONG! The correct answer is: ' + newword.french, font = ('Verdana', 15), bg = '#9999FF' , fg = '#FF0033')

        label_solution.grid(row=5, pady = 10)  

    def nextw(label_solution, word, newword):
        tk.Label(top_start.frame, text = ' ', bg = '#9999FF', padx=200).grid(row=5, pady = 10, ipadx=40)
        entry_answer.delete(0,tk.END)

        word.grid_forget()
        setattr(newword, 'word', random.choice(list(records)))
        setattr(newword, 'german', newword.word[0])
        setattr(newword, 'french', newword.word[1])
        setattr(newword, 'definition', newword.word[2])
        tk.Label(top_start.frame, text = ' ',bg = '#9999FF', padx=400 , pady=15).grid(row=1)
        word = tk.Label(top_start.frame, text = newword.german, font = ('Verdana', 40), bg = '#9999FF', fg = 'black', padx=50 )
        word.grid(row = 1)

    tk.Button(top_start.frame, text = 'CHECK', highlightbackground = '#FFCC00', highlightthickness=6, command =lambda: check(newword, label_solution, entry_answer)).grid(row = 4, column = 0, ipadx = 88, pady = (40,0))
    tk.Button(top_start.frame, text = 'NEXT', highlightbackground = '#FFCC00', highlightthickness=6, command =lambda: nextw(label_solution,  word, newword)).grid(row = 6, column = 0, ipadx = 94, pady = (10,0))
