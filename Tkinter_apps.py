import Math_app.math_app
import Learn_vocabulary.vocabulary
import tkinter as tk
import os

class Myroot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter Apps!')
        self.config(background = '#ffdac3')
        self.geometry('300x450')

        self.frame= tk.Frame(self, bg = '#ffdac3', bd = 0, highlightthickness = 0)
        self.frame.grid(row = 1, pady = (40,100))
        tk.Label(self.frame, text = 'Tkinter Apps',bg = '#ffdac3',fg = '#ff5400', font = ('Comic sans MS', 40)).pack(pady = 10)

        tk.Button (self.frame, text = 'Math app', highlightbackground = '#ffa46d', highlightthickness=6,command = Math_app.math_app.main_import, pady = 20, padx = 30).pack(pady = 10, padx = 30, ipadx = 50)
        tk.Button (self.frame, text = 'Learn vocabulary', highlightbackground = '#ffa46d', highlightthickness=6,command = Learn_vocabulary.vocabulary.main_import, pady = 20, padx = 30).pack(pady = 10, padx = 30, ipadx = 27)
       
        self.closeb = tk.Button (self.frame, text = 'CLOSE PROGRAMM', highlightbackground = 'grey', highlightthickness=6,command = self.destroy,pady = 20, padx = 30)
        self.closeb.pack(pady = 10, ipadx = 20)

main_window = Myroot()

main_window.mainloop()