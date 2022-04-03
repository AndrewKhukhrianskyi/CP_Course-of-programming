'''
from tkinter import *
# HW 03.04

def ivan():
    label['text'] = '01'

def vika():
    label['text'] = '02'

def igor():
    label['text'] = '03'

root = Tk()
root.geometry('200x200')
root.resizable(False, False)

var = IntVar()

rb1 = Radiobutton(text = 'Иван',
                  variable = var,
                  value = 1,
                  command = ivan,
                  indicatoron = 0,
                  width = 5,
                  height = 4)

rb2 = Radiobutton(text = 'Вика',
                  variable = var,
                  value = 2,
                  command = vika,
                  indicatoron = 0,
                  width = 5,
                  height = 4)

rb3 = Radiobutton(text = 'Игорь',
                  variable = var,
                  value = 3,
                  command = igor,
                  indicatoron = 0,
                  width = 5,
                  height = 4)

label = Label(width = 20, 
              height = 2,
              font = '30',
              text = 'Hello')

widgets = [rb1, rb2, rb3]

for wdg in widgets:
    wdg.pack(anchor = W)

label.place(x = 50,
            y = 75)

root.mainloop()

# Alexander - button count

def add_elem():
    elem = int(label['text']) # ''
    elem += 1
    label['text'] = str(elem) # '1'
    

root = Tk()
root.geometry("100x100")
root.resizable(False, False)

label = Label(text = '0',
                    width  = 5,
                    height = 1)

button = Button(text = 'Жмяк!',
                width = 5,
                height = 2,
                command = add_elem)

wdgs = [label, button]

for wdg in wdgs:
    wdg.pack(anchor = N)

root.mainloop()
'''