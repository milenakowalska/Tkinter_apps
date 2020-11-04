
import tkinter as tk
from PIL import ImageTk
import os

class Myroot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn vocabulary!')
        self.config(background = '#9999FF')
        self.geometry('600x550')

        self.image= ImageTk.PhotoImage(file = os.path.join(os.path.dirname(__file__), "multi1.png"))
        self.canvas= tk.Canvas(self, width = 600, height = 200, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.canvas.create_image(300,100, image=self.image)
        self.canvas.grid(row = 0)

        self.frame= tk.Frame(self, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.frame.grid(row = 1, pady = (40,100))

        self.closeb = tk.Button (self, text = 'CLOSE PROGRAMM', highlightbackground = 'grey', highlightthickness=6,command = self.destroy)
        self.closeb.grid(row = 2)

class Mytoplevel(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Learn vocabulary!')
        self.config(background = '#9999FF')
        self.geometry('600x550')

        self.image2= ImageTk.PhotoImage(file = os.path.join(os.path.dirname(__file__), "multi1.png"))
        self.canvas2= tk.Canvas(self, width = 600, height = 200, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.canvas2.create_image(300,100, image=self.image2)
        self.canvas2.pack()
        
        self.frame= tk.Frame(self, bg = '#9999FF', bd = 0, highlightthickness = 0, width = 550, height = 500 )
        self.frame.pack()

        self.closeb = tk.Button (self, text = 'CLOSE WINDOW', highlightbackground = 'grey', highlightthickness=6,command = self.destroy, padx=20)
        self.closeb.pack(pady = 20)

class MyButton(tk.Button):
    def __init__(self, frame, text:str,highlightbackground, command):
        super().__init__(frame) 
        self.config(text = text, highlightbackground=highlightbackground, highlightthickness=6, command = command)

class Word():
    def __init__(self, word):
        self.word = word
        self.german = self.word[0]
        self.french = self.word[1]
        self.definition = self.word[2]
