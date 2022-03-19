import tkinter # Подключаем графическую библиотеку
from random import randint 

def calculate():
    getter_num = int(number.get(0.0))
    getter_num2 = int(number_2.get(0.0))
    lbl = tkinter.Label(text = str(getter_num + getter_num2))
    lbl.place(x = 10, 
              y = randint(10, 100))

screen = tkinter.Tk() # Создаем окно
"""
lab = tkinter.Label(text = 'Один')
lab2 = tkinter.Label(text = 'Два')
lab3 = tkinter.Label(text = 'Три')
lab4 = tkinter.Label(text = 'Четыре')
"""
number = tkinter.Text(width = 5,
                      height = 2)
number_2 = tkinter.Text(width = 5,
                      height = 2)
button = tkinter.Button(text = 'Клик!',
                        width = 10, 
                        height = 2,
                        command = calculate)
screen.geometry('300x300') # Устанавливает размеры окна
screen.title('Классная работа') # Меняет название окна
screen.resizable(False, False) # Изменяем размеры экрана

# W - запад, E - восток, N - север, S - юг
#lab.place(x = 50, y = 150)
#lab2.place(x = 75, y = 155)
#lab3.place(x = 100, y = 160)
#lab4.place(x = 150, y = 165)
number.place(x = 110, y = 110)
number_2.place(x = 125, y = 125)
button.place(x = 150, y = 150)
screen.mainloop() # Безграничная работа
 
