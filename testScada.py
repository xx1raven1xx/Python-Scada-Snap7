# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import snap7
from Fun import *
from threading import Thread
from classes import *
import configparser

client = snap7.client.Client()
stat = client.connect('192.168.1.12', 0, 5)

#DB ={}
sizeDB = 800
DB[110] = client.db_read(110, 0, sizeDB)
DB[104] = client.db_read(104, 0, sizeDB)

#print (get_real(DB[110],620))

def updt():
    t1 = time.time()
    DB[110] = client.db_read(110, 0, sizeDB)                            # Наверное требуется асинхронное чтение ДБшек
    DB[104] = client.db_read(104, 0, sizeDB)
    #print(get_int(DB[104],274))
    t2 = time.time()
    for gameObj in gameObjects:
                gameObj.update()
    c1.itemconfigure(tm, text = (round(t2-t1,4)), fill="red")            # Счетчик времени считывания
    root.after(500, updt)

def test1():
    print("TEST1")

root = Tk()
root.title('Тестовое приложение')

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='R1-R8')
tab_control.add(tab2, text='C1-C12')
tab_control.add(tab3, text='N - B')
tab_control.add(tab4, text='I - H')
tab_control.pack(expand=1, fill='both') 

c1 = Canvas(tab1, width=1800, height=900, bg='black')
c1.pack()
tm = c1.create_text(28, 15, text = 'test', font="System 10")
c2 = Canvas(tab2, width=1800, height=900, bg="#110011")
c2.pack()
c3 = Canvas(tab3, width=1800, height=900, bg="#220011")
c3.pack()
c4 = Canvas(tab4, width=1800, height=900, bg="#110022")
c4.pack()

menu = Menu(tearoff=0)
menu.add_command(label="Редактирование",command=test1)
menu.add_command(label="Остановить обновление",command=test1)
menu.add_command(label="Выйти из программы",command=test1)

x=0
y=0
def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

c1.bind("<Button-3>", popup)


config = configparser.ConfigParser()
#config.add_section("Settings")
config.read("tank.ini")

gameObjects = []

Count_Tank = config.getint("Settings", "count_tank")

for i in range(1, Count_Tank+1):
    if config.getint("TANK{}".format(i), "tab_n") == 1:
        gameObjects.append(Tank(c1, config))
    elif config.getint("TANK{}".format(i), "tab_n") == 2:
        gameObjects.append(Tank(c2, config))
    elif config.getint("TANK{}".format(i), "tab_n") == 3:
        gameObjects.append(Tank(c3, config))
    elif config.getint("TANK{}".format(i), "tab_n") == 4:
        gameObjects.append(Tank(c4, config))


gameObjects.append(Valve(c1, 'VPR3', 300, 500, (104,274)))
gameObjects.append(Valve(c1, 'VPR4', 340, 500, (104,304)))

'''with open("tank.ini", "w") as config_file:
    config.write(config_file)'''


root.after(500, updt)
print('Начало тестирования...')

root.mainloop()