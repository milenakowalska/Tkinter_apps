import tkinter as tk
from PIL import ImageTk
import random
import sqlite3, os
from tkinter import filedialog
from tkinter import ttk

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
        super().__init__(frame) # annotation is only for function 
        self.config(text = text, highlightbackground=highlightbackground, highlightthickness=6, command = command)

class Word():
    def __init__(self, word):
        self.word = word
        self.german = self.word[0]
        self.french = self.word[1]
        self.definition = self.word[2]

def main(main_window):

    # Create database:
    # os.chdir(os.path.dirname(__file__))
    # conn = sqlite3.connect("de2fr2.db")
    # c = conn.cursor()

    # c.execute("""CREATE TABLE words (

    #     german text, 
    #     french text,
    #     definition text
    #     )""")

    # conn.commit()
    # conn.close()

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

    MyButton(main_window.frame,'START', '#CCFF33', start).grid(row = 0, column = 0, ipadx = 116, pady = (40,10))
    MyButton(main_window.frame, 'Add new words', '#FF33CC', add).grid(row = 1, column = 0, ipadx = 88, pady = (10,20))
    MyButton(main_window.frame, 'Show all words','#FFCC00',show).grid(row = 2, column = 0, ipadx = 88)

def main_import():
    main_window = Mytoplevel()
    main(main_window)
    main_window.mainloop()

if __name__ == '__main__':
    main_window = Myroot()
    main(main_window)
    main_window.mainloop()
    
