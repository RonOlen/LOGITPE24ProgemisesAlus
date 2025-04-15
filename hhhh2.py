from tkinter import*

raam= Tk()
raam.title("Pildid")
tahvel = Canvas(raam, width=400, height=400, background="white")

smiley= PhotoImage(file="Nimetu.png")
img = tahvel.create_image(250, 80, image=smiley)

lill = PhotoImage(file="Nimetu2.png")
img = tahvel.create_image(50, 200,image=lill, activeimage=smiley, anchir=NW)

raam.mainloop()