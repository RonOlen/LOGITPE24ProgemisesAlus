from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():  
    tervitus = "Good morning" +nimi.get()
    messagebox.showinfo(message=tervitus)

#tkiteri aken
raam= Tk()
raam.title("CostCo Greeting program")
raam.geometry("300x100")

#tekstikasti silt
silt = ttk.Label(raam, text="Nimi")
silt.grid(column=0,row=0,padx=5,pady=5,sticky=(N,W))

#tekstikast ise
nimi = ttk.Entry(raam)
nimi.grid(column=1,row=1,padx=5,pady=5,sticky=(N,W,E))

#greeting nupp
nupp = ttk.Button(raam, text="Customer greeting", command=tervita)
nupp.grid(column=1,row=1,padx=5,pady=5,sticky=(N,S,E,W))

raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)


#render
raam.mainloop()