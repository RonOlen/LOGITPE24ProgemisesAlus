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
    begin_fill()
    forward (100)
    left (90)
    forward (100)
    left (90)
    forward (100)
    left (90)
    forward (100)
    left (90)
    color(värv)
    end_fill()
    

elif (kujund == "ring"):
    color(värv)
    begin_fill()
    circle(100)
    end_fill()
    
elif (kujund == "ristkülik"):
    color(värv)
    begin_fill()
    left(90)
    forward(100)
    right(90)
    forward(300)
    right(90)
    forward(100)
    right(90)
    forward(300)
    end_fill()
    
elif (kujund == "täisnurkne kolmnurk"):
    color(värv)
    begin_fill()
    lt(90)
    fd(150)
    right(120)
    forward (300)
    left (210)
    forward (270)
    end_fill()
    
elif (kujund == "võrdhaarne kolmnurk"):
    color(värv)
    begin_fill()
    forward (100)
    left (120)
    forward (100)
    left (120)
    forward (100)
    end_fill()
    
    
exitonclick()
