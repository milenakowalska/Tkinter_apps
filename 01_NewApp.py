import tkinter as tk
import os
import webbrowser, sqlite3
from PIL import Image, ImageTk

class MyButton(tk.Button):
    def __init__(self, frame, text, color, command):
        super().__init__(frame)
        self.config(text = text, command=command)
        self.config(highlightbackground=color, font=('courier', 15), highlightthickness=4)

class MyLabel(tk.Label):
    def __init__(self, frame, size, text):
        super().__init__(frame)
        self.config(text = text)
        self.config(bg = 'black', fg='#BDBDBD', font=('courier', size))

class MyEntry(tk.Entry):
    def __init__(self, frame):
        super().__init__(frame)
        self.config(bg='black', fg='#BDBDBD', font=('courier', 15))

    def clean(self):
        self.insert(0, '')

class MyRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Science  App')
        self.geometry = '800x400'
        self.config(bg = 'black')
        self.frame = tk.Frame(self, bg= 'black')
        self.frame.grid(row=0,column=0)
        MyLabel(self.frame, 30, 'Welcome in science App!').grid(row=0,column=0, columnspan=2)
        self.image = ImageTk.PhotoImage(file = os.path.join(os.path.dirname(__file__), 'earth.jpg'))
        self.canvas = tk.Canvas(self, bg = 'black', width = 900, height = 200, highlightthickness=0)
        self.canvas.create_image(400,100,image=self.image)
        self.canvas.grid(row=1,column=0, pady=(40,0))

        MyButton(self.frame, text='Solar System - YouTube', color = 'red', command= lambda:webbrowser.open('https://www.youtube.com/results?search_query=solar+system', new=1)).grid(row=1,column=0, ipadx=40, ipady=5, padx=15, pady=20)
        MyButton(self.frame, text='Solar System - Wikipedia', color = 'red', command= lambda:webbrowser.open('https://en.wikipedia.org/wiki/Solar_System', new=1)).grid(row=1,column=1, ipadx=40, ipady=5, padx=15, pady=20)
        MyButton(self.frame, text='Close App', color = 'grey', command=self.destroy).grid(row=10,column=0, ipadx=56, ipady=5, columnspan=2, pady=30)
        
        self.rows_names = ['Planet name', 'Minimum surface temperature °F', 'Minimum surface temperature °C', 'Maximum surface temperature °F', 'Maximum surface temperature °C']
        self.rows = []
        for index, feld in enumerate(self.rows_names):
            MyLabel(self.frame, 16, text=feld).grid(row=2+index, column=0, pady = 6)

        for index in range(5):
            new_entry = MyEntry(self.frame)
            new_entry.grid(row = 2+index, column = 1)
            self.rows.append(new_entry)
        


class MyTop(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Science  App')
        self.geometry = '800x300'
        self.config(bg = 'black')
        self.frame = tk.Frame(self, bg= 'black')
        self.frame.grid(row=0,column=0)
        MyLabel(self.frame, 30, 'List of planets!').grid(row=0,column=0, columnspan=5)
        self.image = ImageTk.PhotoImage(file = os.path.join(os.path.dirname(__file__), 'earth.jpg'))
        self.canvas = tk.Canvas(self, bg = 'black', width = 900, height = 200, highlightthickness=0)
        self.canvas.create_image(400,100,image=self.image)
        self.canvas.grid(row=1,column=0, pady=(40,0))

        MyButton(self.frame, text='Close window', color = 'grey', command=self.destroy).grid(row=10,column=0, ipadx=56, ipady=5, columnspan=5, pady=30)
        
        

main_window = MyRoot()

## Create table
os.chdir(os.path.join(os.path.dirname(__file__)))
# connection = sqlite3.connect('01_NewApp.db')
# cursor = connection.cursor()

# cursor.execute("""CREATE TABLE planets
# (planet_name, min_fahr, min_cel, max_fahr, max_cel)
# """)
# connection.commit()
# connection.close()

def add_planet():
    planet_values = []
    for feld in main_window.rows:
        planet_values.append(feld.get())
        feld.delete(0,tk.END)

    connection = sqlite3.connect('01_NewApp.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO planets VALUES (:planet_name, :min_fahr, :min_cel, :max_fahr, :max_cel)",
    {
        'planet_name':planet_values[0],
        'min_fahr':planet_values[1],
        'min_cel':planet_values[2],
        'max_fahr':planet_values[3],
        'max_cel':planet_values[4]
    }
    )

    connection.commit()
    connection.close()

def see_planets():
    planets_top = MyTop()

    connection = sqlite3.connect('01_NewApp.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM planets")
    records = cursor.fetchall()

    connection.commit()
    connection.close()

    rows_names = ['Planet name', 'Minimum surface\ntemperature °F', 'Minimum surface\ntemperature °C', 'Maximum surface\ntemperature °F', 'Maximum surface\ntemperature °C']

    for index,name in enumerate(rows_names):
        MyLabel(planets_top.frame, 12, name).grid(row = 1, column=index, padx=15)

    for index,record in enumerate(records):
        for x in range(5):
            MyLabel(planets_top.frame, 16, record[x]).grid(row = index+2, column=x)

MyButton(main_window.frame, text='Add planet to database', color = 'red', command=add_planet).grid(row=7,column=0, ipadx=40, ipady=5, padx=15, pady=20)
MyButton(main_window.frame, text='See a list of planets', color = 'red', command=see_planets).grid(row=7,column=1, ipadx=40, ipady=5, columnspan=2, pady=30)


main_window.mainloop()

