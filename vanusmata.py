# kirjuta programm mis
# küsib kasutajalt kui vana ta on
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt mis on ta lemmikvärv
# Joonista kasutaja lemmikvärvi hulknurk millel on niipalju külgi, kui kasutajal vanust on.
# Selle jaoks on nurkade jaoks sooritada tehe, kus 360 kraadi jagatakse külgede arvuga
# - Kui vanust on rohkem kui 24, joonistatakse lihtsalt ring


from turtle import*


print("Kui vana te olete")
vanus = int(input())
if (vanus < 3):
    print (" Olete liiga noor, ei saa joonistada kujundi teile, womp, womp")
if (vanus > 24):
    print ("  Hästi!, olete vanem kui 24 nüüd ütlege, mis on teie lemmikvärv ja vastage sellele inglise keeles")
    värv = input()
    
    print("Joonistame sulle ringi ")
    color (värv)
    circle (100)
            
else:
    print (" Hästi!, nüüd ütlege, mis on teie lemmikvärv ja vastage sellele inglise keeles")
    värv = input()
    
tehe = 360/vanus
piirjoonmax = 500
valem = piirjoonmax/vanus
print (" nurk tuleb", tehe, "kraadi")
if (vanus == 3):
    color (värv)
forward(valem)
left(tehe)


elif (vanus == 4):
    color (värv)
fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt (90)
fd (100)
    
elif (vanus == 5):
    color (värv)
fd(100)
lt(72)
fd(100)
lt(72)
fd(100)
lt (72)
fd (100)
lt(72)
fd(100)

elif (vanus == 6):
    color (värv)
fd(100)
lt(60)
fd(100)
lt(60)
fd(100)
lt (60)
fd (100)
lt(60)
fd(100)
lt(60)
fd(100)

elif (vanus == 7):
    color (värv)
fd(100)
lt(51)
fd(100)
lt(51)
fd(100)
lt (51)
fd (100)
lt(51)
fd(100)
lt(51)
fd(100)
lt(51)
fd(100)

elif (vanus == 8):
    color (värv)
fd(100)
lt(45)
fd(100)
lt(45)
fd(100)
lt (45)
fd (100)
lt(45)
fd(100)
lt(45)
fd(100)
lt(45)
fd(100)
lt(45)
fd(100)

elif (vanus == 9):
    color (värv)
fd(100)
lt(40)
fd(100)
lt(40)
fd(100)
lt (40)
fd (100)
lt(40)
fd(100)
lt(40)
fd(100)
lt(40)
fd(100)
lt(40)
fd(100)
lt(40)
fd(100)

elif (vanus == 10):
    color (värv)
fd(100)
lt(36)
fd(100)
lt(36)
fd(100)
lt (36)
fd (100)
lt(36)
fd(100)
lt(36)
fd(100)
lt(36)
fd(100)
lt(36)
fd(100)
lt(36)
fd(100)
lt(36)
fd(100)
elif (vanus == 11):
    color (värv)
fd(100)
lt(33)
fd(100)
lt(33)
fd(100)
lt (33)
fd (100)
lt(33)
fd(100)
lt(33)
fd(100)
lt(33)
fd(100)
lt(33)
fd(100)
lt(33)
fd(100)
lt(33)
fd(100)
lt (33)
fd(100)

elif (vanus == 12):
    color (värv)
fd(100)
lt(30)
fd(100)
lt(30)
fd(100)
lt (30)
fd (100)
lt(30)
fd(100)
lt(30)
fd(100)
lt(30)
fd(100)
lt(30)
fd(100)
lt(30)
fd(100)
lt(30)
fd(100)
lt (30)
fd(100)
lt (30)
fd (100)

elif (vanus == 13):
    color (värv)
fd(100)
lt(28)
fd(100)
lt(28)
fd(100)
lt (28)
fd (100)
lt(28)
fd(100)
lt(28)
fd(100)
lt(28)
fd(100)
lt(28)
fd(100)
lt(28)
fd(100)
lt(28)
fd(100)
lt (28)
fd(100)
lt (28)
fd (100)
lt(28)
fd (100)


