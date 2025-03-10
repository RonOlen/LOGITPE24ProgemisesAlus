# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

print (" Kui suur teie põrand on, selleks on vaja meil, teie põranda A külge")
põrandA = int(input())
print (" Nüüd teie B külg")
põrandB = int(input())
pindala = põrandA * põrandB
print ("Põranda pindala on", pindala)


ükss = 10.00
kaks = 11.00
kolm = 15.00
nelii = 20.00
viiss = 25.00
kuuss = 30.00



print (" nüüd vali, millist soovid")
üks = print ("1-██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░")
      print ("  ██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░ 10.00 eur")
teine = print ("2-▄░░ 11.00 eur")
kolmas = print("3-▓▓▒▒ 15.00 eur")
neljas = print("4-░░░ 20.00 eur")
viies = print("5-░▒ 25.00 eur")
kuues = print("6-▓▓▓▓ 30.00 eur")
valik = input()



if (valik == "üks"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus = ükss * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus)
else:
    print("Täname ostu eest")
    
if (valik == "teine"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus1 = kaks * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus1)
else:
    print("Täname ostu eest")


if (valik == "kolmas"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus2 = kolm * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus2)
else:
    print("Täname ostu eest")


if (valik == "neljas"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus3 = nelii * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus3)
else:
    print("Täname ostu eest")


if (valik == "viies"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus4 = viiss * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus4)
else:
    print("Täname ostu eest")


if (valik == "kuues"):
    print ("Olete nõus tasuma selle eest jah/ei?")
    valik = input()
    soodustus5 = kuuss * 0.9
if (valik == "ei"):
    print("Pakkume välja 10% soodustuse et maksad eurodes", soodustus5)
else:
    print("Täname ostu eest")

    
    




