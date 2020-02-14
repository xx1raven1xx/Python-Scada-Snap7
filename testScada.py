# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import snap7
from Fun import *
from threading import Thread
from classes import *

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
    c.itemconfigure(tm, text = (round(t2-t1,4)), fill="red")            # Счетчик времени считывания
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

c = Canvas(tab1, width=1800, height=900, bg='black')
c.pack()
tm = c.create_text(28, 15, text = 'test', font="System 10")
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

c.bind("<Button-3>", popup)



gameObjects = []

gameObjects.append(Tank(c, 'R1', 50, 30, (110,100), (110, 4)))
gameObjects.append(Tank(c, 'R2', 250, 30, (110,104), (110, 8)))
gameObjects.append(Tank(c, 'R3', 450, 30, (110,108), (110, 12)))
gameObjects.append(Tank(c, 'R4', 650, 30, (110,612), (110, 616)))
gameObjects.append(Tank(c, 'R5', 850, 30, (110,620), (110, 624)))
gameObjects.append(Tank(c, 'R6', 450, 330, (110,704), (110, 692)))
gameObjects.append(Tank(c, 'R7', 650, 330, (110,708), (110, 696)))
gameObjects.append(Tank(c, 'R8', 850, 330, (110,712), (110, 700)))

gameObjects.append(Tank(c2, 'C1', 50, 30, (110,420), (110, 324)))
gameObjects.append(Tank(c2, 'C2', 250, 30, (110,424), (110, 328)))
gameObjects.append(Tank(c2, 'C3', 450, 30, (110,428), (110, 332)))
gameObjects.append(Tank(c2, 'C4', 650, 30, (110,432), (110, 336)))
gameObjects.append(Tank(c2, 'C5', 850, 30, (110,436), (110, 340)))
gameObjects.append(Tank(c2, 'C6', 1050, 30, (110,440), (110, 344)))
gameObjects.append(Tank(c2, 'C7', 50, 330, (110,444), (110, 348)))
gameObjects.append(Tank(c2, 'C8', 250, 330, (110,448), (110, 356)))
gameObjects.append(Tank(c2, 'C9', 450, 330, (110,148), (110, 132)))
gameObjects.append(Tank(c2, 'C10', 650, 330, (110,152), (110, 136)))
gameObjects.append(Tank(c2, 'C11', 850, 330, (110,156), (110, 140)))
gameObjects.append(Tank(c2, 'C12', 1050, 330, (110,160), (110, 144)))
gameObjects.append(Tank(c2, 'C13', 1250, 330, (110,684), (110, 688)))

gameObjects.append(Tank(c3, 'N1', 50, 30, (110,124), (110, 28)))
gameObjects.append(Tank(c3, 'N2', 250, 30, (110,128), (110, 32)))

gameObjects.append(Tank(c3, 'B1', 450, 330, (110,260), (110, 164)))
gameObjects.append(Tank(c3, 'B2', 650, 330, (110,264), (110, 168)))
gameObjects.append(Tank(c3, 'B3', 850, 330, (110,268), (110, 172)))

gameObjects.append(Tank(c4, 'I1', 50, 30, (110,272), (110, 176)))
gameObjects.append(Tank(c4, 'I2', 250, 30, (110,276), (110, 180)))
gameObjects.append(Tank(c4, 'I3', 450, 30, (110,280), (110, 184)))

gameObjects.append(Tank(c4, 'H1', 650, 330, (110,112), (110, 16)))
gameObjects.append(Tank(c4, 'H2', 850, 330, (110,116), (110, 20)))
gameObjects.append(Tank(c4, 'H3', 1050, 330, (110,120), (110, 24)))

gameObjects.append(Valve(c, 'VPR3', 300, 500, (104,274)))
gameObjects.append(Valve(c, 'VPR4', 340, 500, (104,304)))


root.after(500, updt)
print('Начало тестирования...')

root.mainloop()
