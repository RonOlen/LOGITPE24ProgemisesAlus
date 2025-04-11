# NB - kõik küsimised on tsüklis, ja joonistamine toimub tkinteriga
#
# kirjuta programm mis
# küsib kasutajalt kui vana ta on
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt mis on ta lemmikvärv inglise keeles
# küsib kasutajalt mis on ta lemmikkujund (tn kolmnurk, võrdkülgne kolmnurk, ruut, ristkülik, ring, ovaal, kaheksanurk)
# Joonista kasutaja lemmikvärvi kujund ja kirjuta kujundi keskele tema vanus

from tkinter import *

raam = Tk()
raam.title("empty tahvel")

tahvel = Canvas(raam, width=600, height=600)

vanus = ""

while (vanus == ""):
    vanus = int(input("Vana te olete?"))
    if (vanus <= 3):
        print("Olete liiga noor")
    if (vanus >= 3):
        varv = input("Mis on teie lemmikvärv? Inglise keeles palun")
        kujund = input("Mis on teie lemmikkujund ? kolmnurk/ruut/võrdkulgne kolmnurk/ristkülik/ring/ovaal/kaheksanurk")
    elif (kujund == "kolmnurk"):
        tahvel.create_polrygon(200,400,200,500,300,500, width=2, outline="black", fill=varv)
        
    elif (kujund == "ruut"):
        tahvel.create_polygon(100,100,100,100, width=2, outline=varv, fill=varv)
        
    elif (kujund == "võrdkülgne kolmnurk"):
        tahvel.create_line(200,200,200,300,300,300,200,200, width=4, fill=varv, arrow = LAST) # x1 y1 x2 y2 x3 y3
        
    elif (kujund == "ristkülik"):
        tahvel.create_rectangle(50,100,100,300, width=2, outline=varv, fill=varv)
        
    elif (kujund == "ring"):
        tahvel.create_ring(400,200,500,300, width=7, outline=varv, fill=varv)
        
    elif (kujund == "ovaal"):
        tahvel.create_oval(400,200,500,300, width=7, outline=varv, fill=varv)
    elif (kujund == "kaheksanurk")
        tahvel.create_ovaal(100,100,200,100,300,200,300,300,200,400,100,400,0,300,0,200 outline="red", fill=varv)

        
        
tahvel.pack()

raam.mainloop()

