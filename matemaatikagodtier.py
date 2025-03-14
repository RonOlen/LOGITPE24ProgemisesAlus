#kirjuta programm mis
# küsib kasutajalt tema lemmivärvi
# kõsib kasutajalt tema lemmikkujundit (ruut, ring , ristkülik, võrdhaarne kolmnurk, täisnurkne kolmnurk
# joonistab kasutajale vastava kujundi tema lemimikvärviga
from turtle import*

print ("Mis teie lemmikvärv on, inglise keeles kirjuta välja?")
värv = input()

print ("Mis on teie lemmikkujund?")
kujund = input()

if (kujund == "ruut"):
    color(värv)
    forward (100)
    left (90)
    forward (100)
    left (90)
    forward (100)
    left (90)
    forward (100)
    left (90)

elif (kujund == "ring"):
    color(värv)
    circle(100)
    
elif (kujund == "ristkülik"):
    color(värv)
    left(90)
    forward(100)
    right(90)
    forward(300)
    right(90)
    forward(100)
    right(90)
    forward(300)
    
elif (kujund == "täisnurkne kolmnurk"):
    color(värv)
    lt(90)
    fd(150)
    right(120)
    forward (300)
    left (210)
    forward (270)
    
elif (kujund == "võrdhaarne kolmnurk"):
    color(värv)
    forward (100)
    left (120)
    forward (100)
    left (120)
    forward (100)
    
    
    
