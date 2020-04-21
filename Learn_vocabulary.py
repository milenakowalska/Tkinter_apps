from tkinter import *
from PIL import ImageTk, Image
import random
import sqlite3
from tkinter import filedialog
from tkinter import ttk

class Myroot(Tk):
    def __init__(self):
        super().__init__()
        self.title('Die geilste App von Mimimimilenka!')
        self.config(background = '#9999FF')
        self.geometry('600x550')

        self.image= ImageTk.PhotoImage(file = "/Users/milenakowalska/Desktop/Python/Tkinter/multi1.png")
        self.canvas= Canvas(self, width = 600, height = 200, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.canvas.create_image(300,100, image=self.image)
        self.canvas.grid(row = 0)

        self.frame= Frame(self, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.frame.grid(row = 1, pady = (40,100))

        self.closeb = Button (self, text = 'CLOSE PROGRAMM', highlightbackground = 'grey', highlightthickness=6,command = self.destroy)
        self.closeb.grid(row = 2)

class Mytoplevel(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Die geilste App von Mimimimilenka!')
        self.config(background = '#9999FF')
        self.geometry('600x550')

        self.image2= ImageTk.PhotoImage(file = "/Users/milenakowalska/Desktop/Python/Tkinter/multi1.png")
        self.canvas2= Canvas(self, width = 600, height = 200, bg = '#9999FF', bd = 0, highlightthickness = 0)
        self.canvas2.create_image(300,100, image=self.image2)
        self.canvas2.pack()
        
        self.frame= Frame(self, bg = '#9999FF', bd = 0, highlightthickness = 0, width = 550, height = 500 )
        self.frame.pack()

class MyButton(Button):
    def __init__(self, frame, text:str,highlightbackground, command):
        super().__init__(frame) # annotation is only for function 
        self.config(text = text, highlightbackground=highlightbackground, highlightthickness=6, command = command)

main_window = Myroot()

# # Database:
conn = sqlite3.connect("de2fr2.db")
c = conn.cursor()
'''
c.execute("""CREATE TABLE words (

    german text, 
    french text,
    definition text
    )""")
'''
conn.commit()
conn.close()

def show():
    top_show = Mytoplevel()

    delet_entry = Entry(top_show.frame, width = 30, bg = '#9999FF')
    delet_entry.pack()

    delet_label = Label(top_show.frame, text = 'Delete a word with ID number: ', bg = '#9999FF')
    delet_label.pack()

    Button(top_show.frame, text = 'Delete a word', highlightbackground = 'black', highlightthickness=6, fg = 'black', command = lambda: delete_word(delet_entry.get())).pack() 

    yscrollbar = Scrollbar(top_show.frame, orient="vertical")
    yscrollbar.pack(side=RIGHT, fill=Y)

    canvas3 = Canvas(top_show.frame, yscrollcommand=yscrollbar.set, bg = '#9999FF', bd = 0, highlightthickness = 0, height = 260, width = 550)
    canvas3.pack(side=LEFT, fill=BOTH)
    yscrollbar.config(command=canvas3.yview)

    connection = sqlite3.connect("de2fr2.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM words")
    records = cursor.fetchall()

    print_rec = str('')

    ind = 0

    inner_frame = Frame(canvas3, width=600, height=(len(records)*40), bg = '#9999FF', bd = 0, highlightthickness = 0)
    canvas3.create_window((0,0), window=inner_frame, anchor='nw')

    for items in records:
        print_rec += str(items[3]) + '\t' + str(items[0]) + ' ---> ' + str(items[1]) +  '\n'
        Label(inner_frame, text = print_rec, bg = '#9999FF').grid(row = ind+ 2, sticky = W)
        ind += 1
        print_rec = str('')

    canvas3.configure(scrollregion=canvas3.bbox("all"))

    connection.commit()
    connection.close()

def delete_word(delet_entry):
    
    connection = sqlite3.connect("de2fr2.db")
    cursor = connection.cursor()
    cursor.execute('DELETE from words WHERE oid= ' + delet_entry)      
    connection.commit()
    connection.close() 

def submit(german, french, definition):

    conn = sqlite3.connect("de2fr2.db")
    c = conn.cursor()
    c.execute("INSERT INTO words VALUES(:german, :french, :definition)", 
        {
                'german' : german.get(),
                'french' : french.get(),
                'definition' : definition.get()
        })
    conn.commit()
    conn.close()

    german.delete(0,END)
    french.delete(0,END)
    definition.delete(0,END)

def add():

    top_add = Mytoplevel()

    german = Entry(top_add.frame, width = 30, bg = '#9999FF')
    german.grid(row = 0, column = 1)
    french = Entry(top_add.frame, width = 30, bg = '#9999FF')
    french.grid(row = 1, column = 1)
    definition = Entry(top_add.frame, width = 30, bg = '#9999FF')
    definition.grid(row = 2, column = 1)

    number = 0
    for element in ('German','French','Definition'):
        Label(top_add.frame, text = str(element), bg = '#9999FF').grid(row = number, column = 0)
        number +=1

    submit_button = Button(top_add.frame, text = 'Add a new word!', highlightbackground = '#FF6633',highlightthickness=6, command =lambda: submit(german, french, definition))
    submit_button.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 113)

def start(): 
    top_start = Mytoplevel()

    ### Choose the random element from dictionary file

    connection = sqlite3.connect("de2fr2.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM words")
    records = cursor.fetchall()
    connection.commit()
    connection.close()

    newo = random.choice(list(records))
    ###
    word = Label(top_start.frame, text = newo[0], font = ('Verdana', 40), bg = '#9999FF', fg = 'black' )
    word.grid(row = 1)

    Label(top_start.frame, text = 'Write the word in French', font = ('Verdana', 15), bg = '#9999FF' ).grid(row=2, pady = 10)

    entry_answer = Entry(top_start.frame, bg = '#9999FF')
    entry_answer.grid(row = 3)

    label_solution = Label(top_start.frame, text = '', bg = '#9999FF')
    label_solution.grid(row=5, pady = 10) 

    def check(newo, label_solution, entry_answer):
        label_solution.grid_forget()
        answer = str(entry_answer.get())

        if str(newo[1]) == answer:
            label_solution =  Label(top_start.frame, text = 'CORRECT!', font = ('Verdana', 15), bg = '#9999FF' , fg = '#006600')
        else:
            label_solution = Label(top_start.frame, text = 'WRONG! The correct answer is: ' + newo[1], font = ('Verdana', 15), bg = '#9999FF' , fg = '#FF0033')

        label_solution.grid(row=5, pady = 10)  

    def nextw(label_solution, word, newo):
        label_solution.grid_forget()
        label_solution = Label(top_start.frame, text = ' ', bg = '#9999FF')
        label_solution.grid(row=5, pady = 10) 

        entry_answer.delete(0,END)

        word.grid_forget()
        newo = random.choice(list(records))

        word = Label(top_start.frame, text = newo[0], font = ('Verdana', 40), bg = '#9999FF', fg = 'black' )
        word.grid(row = 1)

    Button(top_start.frame, text = 'CHECK', highlightbackground = '#FFCC00', highlightthickness=6, command =lambda: check(newo, label_solution, entry_answer)).grid(row = 4, column = 0, ipadx = 88, pady = (40,0))
    Button(top_start.frame, text = 'Close window', highlightbackground = 'grey', highlightthickness=6, command = top_start.destroy).grid(row = 7, column = 0, ipadx = 68, pady = (10,0))
    Button(top_start.frame, text = 'NEXT', highlightbackground = '#FFCC00', highlightthickness=6, command =lambda: nextw(label_solution,  word, newo)).grid(row = 6, column = 0, ipadx = 94, pady = (10,0))

MyButton(main_window.frame,'START', '#CCFF33', start).grid(row = 0, column = 0, ipadx = 116, pady = (40,10))
MyButton(main_window.frame, 'Add new words', '#FF33CC', add).grid(row = 1, column = 0, ipadx = 88, pady = (10,20))
MyButton(main_window.frame, 'Show all words','#FFCC00',show).grid(row = 2, column = 0, ipadx = 88)
main_window.mainloop()