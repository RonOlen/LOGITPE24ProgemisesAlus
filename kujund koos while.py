# küsib kasutajalt kui vana ta on
# küsib kasutajalt kui pikk ta on meetrites
# küsib kasutajalt tema ees ja perekonnanime
# küsib kasutajalt kas talle meeldivad geomeetrilised kujundid
# kui kasutaja vastab jah, siis küsitakse kasutajalt terve rida küsimusi järgnevate kujundite kohta: (ring, ruut, kolmnurk, ovaal)
# - kas talle meeldib <kujund>
# - kui kasutaja vastab <kujund>i kohta jah, siis peab programm meelde jätma et kasutaja tahab seda kujundit eraldi muutujas
# - kasutajalt küsitakse ka tema lemmikvärvi kohta, mille jaoks antakse kasutajale inglisekeelne valik
# - seejärel joonistab programm kõik kujundid mis said "jah" vastuse kasutaja lemmikvärviga ekraanile +
# - kujundite küljepikkus tuleb läbi korrutada kasutaja pikkusega. kujundite standardküljepikkus on 100px
# - Viimasena joonistatakse ekraanile teksti abil sõnum "palun"<kasutajanimi>"siin on sinu lemmikkujundid"<värv> värviga

from tkinter import*


vanus = ""
pikkus = ""
nimi = ""


raam = Tk()
raam.title("sigma tahvel")

tahvel = Canvas(raam, width = 600, height = 600)


while (nimi == "" or pikkus == "" or vanus == ""):
    vanus = int(input(" kui vana te olete?"))
    pikkus = int(input("Kui pikk te olete?"))
    nimi = input("Mis on teie ees ja perekonnanimi")
    kujundarvamus = input("Kas teile meeldivad geomeetrilised kujundid")
if (kujundarvamus == "jah"):
    print("Anname teile kujundi variendid valige välja, mis kujund teile meeldib")
    ring = input("Ring jah/ei.")
    ruut = input("Ruut jah/ei")
    kolmnurk = input("Kolmnurk jah/ei")
    ovaal = input("Ovaal jah/ei")
    
    if ring == "jah" or ruut == "jah" or kolmnurk == "jah" or ovaal == "jah":
        varv = input("Mis on teie lemmikvärv inglise keeles? red/blue/green/white/black/yellow")

        
          
    if (ring == "jah"):
        tahvel.create_oval(400,200,500,300,outline=varv, fill=varv)
          
    if (ruut == "jah"):
        tahvel.create_rectangle(100,100,200,200, width=2, outline=varv, fill=varv)
          
    if (kolmnurk == "jah"):
        tahvel.create_polygon(450,400,450,500,550,500, width=2, outline=varv, fill=varv)
          
    if (ovaal == "jah"):
        tahvel.create_oval(100,200,300,600, width=7, outline=varv, fill=varv)
          
          
tahvel.pack()

raam.mainloop()


    