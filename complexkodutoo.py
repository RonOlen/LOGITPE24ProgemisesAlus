
# kirjuta programm mis:
# küsib kasutajalt tsükli sees kui palju raha ta panustada soovib
# - kui kasutaja sisestab positiivse arvväärtuse, tsükkel lõppeb ja programm läheb järgmise osa juurde
# - kui kasutaja sisestab negatiivse arvväärtuse, siis öeldakse kasutajale et on vaja positiivset rahasummat ja küsimus küsitakse uuesti
# - kui kasutaja jätab arvu üldse kirjutamata või kirjutab teksti, siis öeldakse kasutajale, et on vaja positiivset rahasummat
# - ja küsimus küsitakse uuesti
# NB! - draakonil on sama arv raha, kui on mängijal, aga selleks ei kasutata ühte sama muutujat
# järgmine osa toimub teise tsükli sees niikaua kuni mängijal raha otsas ei ole või niikaua kuni draakonil raha otsas ei ole:
# - draakon küsib palju sisestatud rahasummast ta see mänguring panustada soovib.
# - - panus ei saa olla suurem kui rahasumma mis kasutaja algselt sisestas.
# - draakon küsib kas arv on suurem kui see arv, mis tema kolm kuuekülgset täringut kokku saavad.
# - kasutaja sisestab arvu
# - juhuarvu abil, veeretatakse kolme kuuekülgset täringut
# - - kui kasutaja arvab õigesti, annab draakon talle 2x esialgset panust
# - - kui kasutaja arvab valesti on ta oma eelnevast panusest ilma
# - mängija võidab siis kui draakonil on näpud põhjas
# - draakon küsib mängijalt peale igat mänguringi kas ta soovib oma võidud välja võtta ning mängulauast lahkuda
# - - kui kasutaja vastab ei, jätkub mäng nagu tavaliselt
# - - kui kasutaja vastab jah, ütleb draakon mängijale siin on sinu võidud (peab panema kui palju mängija oma algsummale juurde võitis), ootan sind ja sinu raha siia tagasi...
from random import randint


print (" Palju chipe te ostade?")
betsumma = int(input())
fake = input()
real = input()


while ( betsumma < 1):
    print (" on vaja panna positiivne summa")
    print (" Kas olete valmis panustama?")
    panus int(imput())
    
    
while ( betsumma == ""):
    print (" Sul on vaja sisesta positiivne arv")
else:
    print(" Sul on vaja sisestada positiivne arv")
    
while ( betsumma > 1):
    print("Hästi lähme järgmise etappi juurde")

print(" vali number 1-6")
number = int(input())
dice = randint(1.18)
if (number == dice):
    tehe = number *2
    print("Oled võitija!")
    print (" Sinu summa on",tehe)
else:
    kaotus = fake - betsumma
    print (" Kaotasid su summa on nyyd",kaotus,)
