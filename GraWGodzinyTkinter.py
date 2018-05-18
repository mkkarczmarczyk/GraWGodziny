from Tkinter import *
import math
import random
import tkMessageBox
import collections

master = Tk()
master.title("Jaka jest teraz godzina?")
w = Canvas(master, width=300, height=300)
w.pack()

#godziny={'IX': '9', 'XI': '11', 'I': '1', 'VI': '6', 'VII': '7', 'IV': '4', 'II': '2', 'VIII': '8', 'XII': '12', 'V': '5', 'X': '10', 'III': '3'}
#minuty={'IX': '45', 'VI': '30', 'XI': '55', 'I': '05', 'XII': '00', 'VII': '35', 'IV': '20', 'II': '10', 'VIII': '40', 'V': '25', 'X': '50', 'III': '15'}

#godziny={'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','11':'XI','12':'XII'}
#minuty={'05':'I','10':'II','15':'III','20':'IV','25':'V','30':'VI','35':'VII','40':'VIII','45':'IX','50':'X','55':'XI','00':'XII'}

godziny=['1','2','3','4','5','6','7','8','9','10','11','12']
minuty=['00','05','10','15','20','25','30','35','40','45','50','55']

def rysuj_wskazowki (godz,minuta):
    for i in range (0,360,30):
        dx=150; dy=150; r=100
        rad_fi=i*3.14/180
        x = int( r * math.sin(rad_fi)) + dx
        y = int( r * math.cos(rad_fi)) + dy
        w.create_line(x,y,x+5,y,fill='green',width=2)
    #dx=150; dy=150
    wskaz_godz_dlugosc=70
    wskaz_minut_dlugosc=80
    kat_godz=0.5*3.14/180*(60*godz+minuta)
    kat_minuta=minuta*3.14*6/180
    x_godz=int( wskaz_godz_dlugosc * math.sin(3.14-kat_godz))+dx
    y_godz=int( wskaz_godz_dlugosc* math.cos(3.14-kat_godz))+dy
    x_minuta=int( wskaz_minut_dlugosc * math.sin(3.14-kat_minuta)) +dx
    y_minuta=int( wskaz_minut_dlugosc * math.cos(3.14-kat_minuta)) +dy
    w.create_line(150,150,x_godz,y_godz, fill='red',width=5)
    w.create_line(150,150,x_minuta,y_minuta, fill='blue',width=2)

def generuj():
    global godz,minuta
    godz=random.choice(godziny)
    minuta=random.choice(minuty)
    rysuj_wskazowki(int(godz),int(minuta))
    return godz,minuta

def callback():
    #global entryWidget
    #print str(E1Val)
    if E1.get(E1.curselection()) == godz and E2.get(E2.curselection())==minuta:
        tkMessageBox.showinfo("Info", "Zuch")
        w.delete('all')
        generuj()
    else:
        tkMessageBox.showerror("Info", "Jeszcze raz" )




textFrame = Frame(master)


L1 = Label(textFrame, text="Godzina")
L1.pack(side = LEFT)

scrollbar1 = Scrollbar(textFrame)

E1 = Listbox(textFrame,exportselection=0,height=5,width=5,yscrollcommand=scrollbar1.set)



for key in godziny:
    E1.insert(END, key)


E1.pack(side = LEFT,fill=Y)
scrollbar1.pack(side=LEFT, fill=Y)
scrollbar1.config(command=E1.yview)


L2 = Label(textFrame, text="Minut")
L2.pack( side = LEFT,fill=None)

scrollbar2 = Scrollbar(textFrame)
E2 = Listbox(textFrame,exportselection=0,height=5,width=5,yscrollcommand=scrollbar2.set)
for key in minuty:
    E2.insert(END, key)

scrollbar2.pack(side=RIGHT, fill=Y)
scrollbar2.config(command=E2.yview)
E2.pack(side=LEFT)



textFrame.pack()



button = Button(master, text="OK", command=callback)
button.pack(fill=X,pady=5)

generuj()
mainloop()
