from Fun import *
DB ={}              # плохо что приходится использовать эту переменную и тут, и в главном файле программы
count = 0

class Valve:
    def __init__(self, canvas, name, x, y, DB = (104, 0)):
        # класс клапана, создание и обновление
        self.valveX = x
        self.valveY = y
        self.DB = DB
        self.canvas = canvas
        self.vlv = canvas.create_polygon(10+self.valveX,10+self.valveY,40+self.valveX,10+self.valveY,10+self.valveX,50+self.valveY,40+self.valveX,50+self.valveY,fill='green',outline='white')
    def update(self):
        global DB
        if get_int(DB[self.DB[0]],self.DB[1]) == 2:
            self.canvas.itemconfigure(self.vlv, fill = 'red', outline='yellow')
        elif get_int(DB[self.DB[0]],self.DB[1]) == 4:
            self.canvas.itemconfigure(self.vlv, fill = 'green', outline='blue')
        else:
            self.canvas.itemconfigure(self.vlv, fill = 'grey', outline='white')


class Tank:
    def __init__(self, canvas, Name, x, y, LIC = (110, 4),TIC = (110, 4)):
        # класс бочки, создание и обновление. вертикальный прогресбар + лика + температура (в будущем и вывод имени сырья в бочке)
        self.tankX = x #50
        self.tankY = y #30
        self.LIC = LIC
        self.TIC = TIC
        self.canvas = canvas
        self.canvas.create_polygon(self.tankX, 30+self.tankY, 92+self.tankX, self.tankY-6, 184+self.tankX, 30+self.tankY, 184+self.tankX, 204+self.tankY, self.tankX, 204+self.tankY,fill='grey',outline='white')
        self.canvas.create_text(40+self.tankX, 45+self.tankY, text = Name, font="System 25")

        self.canvas.create_rectangle(157+self.tankX,33+self.tankY,179+self.tankX,199+self.tankY,fill='grey',outline='red')
        valueLevel = 0                                                                                       # Тут пересчет высоты столбика
        spareLevel = (162*valueLevel)/100 + (35+self.tankY)
        self.bar = self.canvas.create_rectangle(159+self.tankX, spareLevel,177+self.tankX,197+self.tankY,fill='orange')

        self.canvas.create_rectangle(20+self.tankX,80+self.tankY,(145+self.tankX),(110+self.tankY),fill='yellow',outline='green')       # желтая рамка LICA
        self.canvas.create_text(50+self.tankX, 90+self.tankY, text="TIC", font="Verdana 10")  #justify=CENTER                          # надпись LICA
        self.tic1 = self.canvas.create_text(100+self.tankX, 102+self.tankY, text='00.00')                                                # вывод значений LICA

        self.canvas.create_rectangle(20+self.tankX,130+self.tankY,(145+self.tankX),(160+self.tankY),fill='yellow',outline='green')       # желтая рамка LICA
        self.canvas.create_text(50+self.tankX, 140+self.tankY, text="LICA", font="Verdana 10")  #justify=CENTER                          # надпись LICA
        self.lic1 = self.canvas.create_text(100+self.tankX, 152+self.tankY, text='00.00')                                                # вывод значений LICA

    def update(self):
        global DB
        self.canvas.itemconfigure(self.tic1, text = round(get_real(DB[self.TIC[0]],self.TIC[1]), 2))
        self.canvas.itemconfigure(self.lic1, text = round(get_real(DB[self.LIC[0]],self.LIC[1]), 2))
        self.canvas.coords(self.bar, 159+self.tankX, (35+self.tankY) + (162-((162*(round(get_real(DB[self.LIC[0]],self.LIC[1]), 3)))/100)),177+self.tankX,197+self.tankY)


