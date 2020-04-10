import tkinter as tk
from PIL import ImageTk, Image
import random, os

class Mylabel(tk.Label):
    def __init__(self, frame, text, size):
        super().__init__(frame)
        self.config(text=text, padx=40)
        self.config(fg="#99FFFF", bd=0, highlightthickness=0, bg="#339999", pady=5, font=("Verdana", size))
        
class Mybutton(tk.Button):
    def __init__(self, frame, text, padx, color, command):
        super().__init__(frame)
        self.config(text=text, command=command, padx=padx, highlightbackground=color)
        self.config(pady=5, highlightthickness=4, font=("Verdana", 15, "bold"))

class Myentry(tk.Entry):
    def __init__(self, frame, color, fgcolor, text=None):
        super().__init__(frame)
        if text is not None:
            self.insert(0, text)
            self.value = text
        else:
            self.value = 0

        self.config(bg=color, fg=fgcolor, font=("Verdana", 15, "bold"), width=3)

class Myrow(Myentry):
    def __init__(self, frame, row, category):
        self.row = row
        self.entry1 = Myentry(frame, "#339999", "white")
        self.entry1.grid(row=row, column=0)
        Mylabel(frame, category, 15).grid(row=row, column=1)
        self.entry2 = Myentry(frame, "#339999", "white")
        self.entry2.grid(row=row, column=2)
        Mylabel(frame, "=", 15).grid(row=row, column=3)
        self.entry_response = Myentry(frame, "#339999", "white")
        self.entry_response.grid(row=row, column=4)
        self.solution = Mylabel(frame, "       ", 15).grid(row=row, column=5)

class Myroot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elementary arithmetic test")
        self.config(background="#339999")
        self.geometry("1000x500")
        self.image = ImageTk.PhotoImage(file= os.path.join(os.path.dirname(__file__), "brain.png"))
        self.canvas = tk.Canvas(self, bg="#339999", width=500, height=500, highlightthickness=0)
        self.canvas.create_image(250, 250, image=self.image)
        self.canvas.grid(row=0, column=0)

        self.frame = tk.Frame(self, highlightthickness=0, bg="#339999")
        self.frame.grid(row=0, column=1)

class Mytop(tk.Toplevel):
    def __init__(self, name):
        super().__init__()
        self.title("Elementary arithmetic test")
        self.config(background="#339999")
        self.geometry("1150x500")

        self.image = ImageTk.PhotoImage(file= os.path.join(os.path.dirname(__file__), "brain.png"))
        self.canvas = tk.Canvas(self, bg="#339999", width=500, height=500, highlightthickness=0)
        self.canvas.create_image(250, 250, image=self.image)
        self.canvas.grid(row=0, column=0)

        self.frame = tk.Frame(self, highlightthickness=0, bg="#339999")
        self.frame.grid(row=0, column=1)

        self.timer_label = tk.Label(self.frame, text="00:00:00", font="verdana 80", bg="#339999", fg="white", padx=50, pady=5)
        self.timer_label.grid(row=1, column=0, columnspan=3)
        Mylabel(self.frame, name, 30).grid(row=0, column=0, columnspan=7, pady=(0, 20))
        Mybutton(self.frame, "Close window", 40, "grey", self.destroy).grid(row=10, column=0, columnspan=7, ipadx=129.5, pady=(20, 0))

class Timer:
    """This is timer class"""
    def __init__(self):
        self.hours = 00
        self.minutes = 00
        self.seconds = 00
        self.count = 0
        self.mytime = "00:00:00"
        self.showseconds = 00

    @property
    def resetcount(self):
        self.count = 0

    @resetcount.setter
    def resetcount(self, newc):
        self.count = newc
        self.seconds = 00
        self.minutes = 00
        self.hours = 00
        self.showseconds = 00

mainwindow = Myroot()

def test(command):
    if command == 'addition':
        test_top = Mytop("Addition test")
        category = '+'
    elif command == 'subtraction':
        test_top = Mytop("Subtraction test")
        category = '-'
    elif command == 'multiplication':
        test_top = Mytop("Multiplication test")
        category = '*'
    elif command == 'division':
        test_top = Mytop("Division test")
        category = '/'

    examples = []
    count = 2
    for example in range(5):
        row = Myrow(test_top.frame, count, category)
        examples.append(row)
        count += 1

    add_pasttime = Timer()
    test_top.timer_label["text"] = add_pasttime.mytime
    test_top.timer_label.grid(row=1, column=0, columnspan=6)

    def reset():
        add_pasttime.resetcount = 1
        test_top.timer_label["text"] = add_pasttime.mytime

    def stop():
        add_pasttime.resetcount = 2

    def display_time():
        if add_pasttime.count == 0:

            add_pasttime.minutes = int(add_pasttime.minutes)
            add_pasttime.hours = int(add_pasttime.hours)

            add_pasttime.seconds += 5 / 3
            if add_pasttime.seconds > 99:
                add_pasttime.seconds = 00
                add_pasttime.minutes += 1
                if add_pasttime.minutes > 59:
                    add_pasttime.minutes = 00
                    add_pasttime.hours += 1
            add_pasttime.showseconds = int(add_pasttime.seconds)

            if len(str(add_pasttime.showseconds)) == 1:
                add_pasttime.showseconds = "0" + str(add_pasttime.showseconds)
            if len(str(add_pasttime.minutes)) == 1:
                add_pasttime.minutes = "0" + str(add_pasttime.minutes)
            if len(str(add_pasttime.hours)) == 1:
                add_pasttime.hours = "0" + str(add_pasttime.hours)

            test_top.timer_label["text"] = "{}:{}:{}".format(str(add_pasttime.hours), str(add_pasttime.minutes), str(add_pasttime.showseconds))
            test_top.timer_label.after(10, display_time)

    def show_test():
        if command == 'addition' or command == 'subtraction':
            for each in examples:
                each.entry1.insert(0, random.randint(0, 100))
                each.entry2.insert(0, random.randint(0, 100))

        elif command == 'multiplication':
            for each in examples:
                each.entry1.insert(0, random.randint(0, 20))
                each.entry2.insert(0, random.randint(0, 20))
        
        elif command == 'multiplication':
            for each in examples:
                each.entry1.insert(0, random.randint(0, 20))
                each.entry2.insert(0, random.randint(0, 20))
        
        elif command == 'division':
            for each in examples:
                first = random.randint(10, 200)
                each.entry1.insert(0, first)
                divisors = []
                while not divisors:
                    for number in range (2, first):
                        if first % number == 0 and number != 0:
                            divisors.append(number)
                each.entry2.insert(0, random.choice(divisors))

    def start_add():
        add_pasttime.resetcount = 0
        display_time()
        show_test()

    def check_add():
        stop()
        for each in examples:
            setattr(each.entry1, "value", each.entry1.get())
            setattr(each.entry2, "value", each.entry2.get())
            setattr(each.entry_response, "value", each.entry_response.get())

            if command == 'addition':
                if int(each.entry1.value) + int(each.entry2.value) == int(each.entry_response.value):
                    Mylabel(test_top.frame, "RIGHT", 15).grid(row=each.row, column=5)
                else:
                    Mylabel(test_top.frame, "WRONG", 15).grid(row=each.row, column=5)

            if command == 'subtraction':
                if int(each.entry1.value) - int(each.entry2.value) == int(each.entry_response.value):
                    Mylabel(test_top.frame, "RIGHT", 15).grid(row=each.row, column=5)
                else:
                    Mylabel(test_top.frame, "WRONG", 15).grid(row=each.row, column=5)
        
            if command == 'multiplication':
                if int(each.entry1.value) * int(each.entry2.value) == int(each.entry_response.value):
                    Mylabel(test_top.frame, "RIGHT", 15).grid(row=each.row, column=5)
                else:
                    Mylabel(test_top.frame, "WRONG", 15).grid(row=each.row, column=5)
        
            if command == 'division':
                if int(each.entry1.value) / int(each.entry2.value) == int(each.entry_response.value):
                    Mylabel(test_top.frame, "RIGHT", 15).grid(row=each.row, column=5)
                else:
                    Mylabel(test_top.frame, "WRONG", 15).grid(row=each.row, column=5)

    Mybutton(test_top.frame, "START", 40, "yellow", start_add).grid(row=9, column=0, columnspan=2, ipadx=10, pady=(10, 0), padx=6)
    Mybutton(test_top.frame, "CHECK", 40, "yellow", check_add).grid(row=9, column=3, columnspan=2, ipadx=10, pady=(10, 0), padx=6)

Mylabel(mainwindow.frame, "Elementary arithmetic test", 30).grid(row=0, column=0, columnspan=2, pady=(0, 60))
Mylabel(mainwindow.frame, "Choose category:", 20).grid(row=1, column=0, columnspan=2, sticky="W" + "E")

Mybutton(mainwindow.frame,'Addition', 10, 'yellow', lambda: test('addition')).grid(row = 3, column = 0, padx=10, pady = 10, sticky = 'W'+'E')
Mybutton(mainwindow.frame, 'Subtraction', 10, 'yellow', lambda: test('subtraction')).grid(row = 3, column = 1, padx=10, pady = 10, sticky = 'W'+'E')
Mybutton(mainwindow.frame, 'Multiplication', 10, 'yellow', lambda: test('multiplication')).grid(row = 4, column = 0, padx=10, pady = 10, sticky = 'W'+'E')
Mybutton(mainwindow.frame, 'Division', 10, 'yellow', lambda: test('division')).grid(row = 4, column = 1, padx=10, pady = 10, sticky = 'W'+'E')

Mybutton(mainwindow.frame, "Close program", 40, "grey", mainwindow.destroy).grid(row=10, column=0, columnspan=2, ipadx=129.5, pady=(70, 0))

mainwindow.mainloop()
