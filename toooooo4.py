from tkinter import *

raam = Tk()
raam.title("empty tahvel")

tahvel = Canvas(raam, width=600, height=600)

#elemendid

#jooned
tahvel.create_line(50,50,100,50) #x1 y1 x2 y2
tahvel.create_line(200,200,200,300,300,300,200,200, width=4, fill="green", arrow = LAST) # x1 y1 x2 y2 x3 y3

#ristkülikud
tahvel.create_rectangle(50,100,100,300, width=2, outline="orange", fill="yellow")
#(x1 y1 x2 y2, kujundi serva paksus, kujundi serva värv, kujudi täitevarv

#polygon
tahvel.create_polygon(200,400,200,500,300,500, width=2, outline="black", fill="cyan")

#ovaal/ring
tahvel.create_oval(400,200,500,300, width=7, outline="red", fill="orange")
tahvel.create_oval(500,200,600,500, width=7, outline="red", fill="orange")

#telst
tahvel.create_text(300,300, text="Hällo würl", fill="blue")


tahvel.pack()

raam.mainloop()