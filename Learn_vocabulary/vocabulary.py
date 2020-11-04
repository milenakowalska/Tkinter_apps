from PIL import ImageTk
import sqlite3, os

from my_classes import Myroot, Mytoplevel, MyButton, Word
from show import show
from add import add
from start import start

##  Create database:

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

def main(main_window):
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
    
