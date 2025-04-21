# kõik küsimised tsükliga
# kõik joonistamised tsükliga
# küik sisendid töödelda
#
# kirjuta programm mis
# küsib kasutajalt tema tunnusjooni
# mis on ta nahavärv ("kasutaja ütleb inglisekeelse värvi")
# kas tal on müts (kui jah siis valikus on nokamüts, torumüts ja fedora, kui ei, siis joonista juuksed)
# milline tuju tal on (hea C:, tavaline :I, halb :C, üllatunud :O, tülpinud I:C)
# ja mis ilm on (pilvitu = sinine taust, pilvine = valge taust, vihmane= hall taust, )
# programm tagastab pildi kasutajale temast praegusel ajahetkel.

from tkinter import *

nahavarv = ""
tunnusjoon = ""
müts = ""
tuju = ""
mütsvalik = ""
valik = ""
ilm = ""

raam=Tk()
tahvel = Canvas(raam, width=500, height=500)

while (nahavarv == "" or tunnusjoon == "" or müts == "" or tuju == "" or ilm == "" or mütsvalik == "" or valik == ""):
    if (nahavarv == ""):
        nahavarv = input(" Mis on teie nahavarv")
    if (müts == ""):
        müts = input("Kas teil on müts jah/ei")
    if müts == "jah":
        müts = input("Kas teil on Nokamüts/Torumüts/Fedora?")
    if (tuju == ""):
        tuju = input(" Milline tuju teil on? Hea/Tavaline/Halb/Üllatunud/Tülpinud")
    if (ilm == ""):
            ilm = input("Milline on ilm?: Pilvitu/pilvine/vihmane")
            
            
if (nahavarv.lower() == "hele"):
    nahavarv = "FFCCE0"
elif (nahavarv.lower() == "kergepäevitunud"):
    nahavarv = ("DEAD4B")
elif (nahavarv.lower() == "punanahk"):
    nahavarv = "DE7C4B"
elif (nahavarv.lower() == "pronksjas"):
    nahavarv = "8C390F"
elif (nahavarv.lower() == "tume"):
    nahavarv = "#F1E05"
    
def joonistaNägu(nahavarv,müts):
    tahvel.create_oval(50,50,450,450,fill=nahavarv,outline="black",width=5)
    tahvel.create_oval(140,140,160,160,fill="green",outline="black",width=2)
    tahvel.create_oval(340,140,360,160,fill="green",outline="black",width=2)
    if müts.lower() == "nokamüts":
        tahvel.create_polygon(100,100,200,100,200,75, 250,25, 300,25, 400, 75, 400, 100,fill="red",outline="black",width=5)
    if müts.lower() == "torumüts":
        tahvel.create_polygon(50,100,150,100, 150,0, 350,0, 350, 100, 450,100, fill="gray",outline="black",width=5)
    if müts.lower() == "fedora":
        tahvel.create_oval(15,25,350,100,fill="yellow",outline="black",width=5)    
    else:
        tahvel.create.polygon(93,24,77,146,117,245,130,317,112,412,132,392,17,363,40,331,17,307,40,268,17,181,40,153,17,122,40,93,17, outline="black")
    if (tuju.lower()) == "hea":
        tahvel.create.arc(150, 335, 365, 336,)
    elif (tuju.lower()) == "tavaline":
        tahvel.create.line(150,382,172,345,218,336,285,336,335,345,362,382, fill="black", width = 10)
    elif (tuju.lower()) == "halb":
        tahvel.create.line(150,382,172,345,218,336,285,336,336,345,365,382, fill = "black", width=10)
    elif (tuju.lower()) == "üllatanud":
        tahvel.create.line(150,336,350,382, fill="brown", outline="black", width = 10)
    elif (tuju.lower()) == "tülpinud":
        tahvel.create.line(150,382, 172, 345, 218, 336, 285, 336, 336, 345, 362, 382, fill="black", width =10)
        tahvel.create.line(125,200,175,230, width=10)
        tahvel.create.line(325,230,375,200, width=10)


    else:
        print(" Kasutaja tuju ei ole õige asi, palun proovige jalle")
        
    if ilm.lower() == "pilvitu":
        tahvel.configure(bg="lightblue")
    elif ilm.lower() == "pilvine":
        tahvel.configure(bg="white")
    elif ilm.lower() == "vihmane":
        tahvel.configure(bg="darkgray")

    
joonistaNägu(nahavarv,müts,tuju,ilm)            
            
tahvel.pack()
raam.mainloop()
            
            


                     

                     