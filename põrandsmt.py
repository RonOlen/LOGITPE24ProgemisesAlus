	Tund (6. - 9. Tund) /
Tsükkel 6 Nädal 27 N-asendus
 
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
 
laius = int(input("Kui lai on sinu põrand?: "))
pikkus = int(input("Kui pikk on sinu põrand?: "))
print("Palun vali allolevatest mustritest omale sobiv põrandaplaadimuster:")
print("1 - ██░░ 2 - ║┌─┐ 3 - ▀▄░░ 4 - ░░┌┐ 5 - ▀▄▀▄ 6 - ██▀▄\n ░░██ ║└─┘ ░░▀▄ ░░└┘ ▀▄▀▄ ▀▄██")
kasutajaValik = int(input("Vali muster numbriga 1-6, millise valid?: "))
muster1 = 1.2
muster2 = 1.75
muster3 = 2.12
muster4 = 3.05
muster5 = 3.45
muster6 = 5.5
hetkekordaja = 0
summa = 0
põrand = laius*pikkus
if (kasutajaValik == 1):
hetkekordaja = muster1
print("██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░\n░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░\n░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░\n░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██\n██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░\n░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██\n")
elif (kasutajaValik == 2):
hetkekordaja = muster2
print("║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐\n║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘\n║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐\n║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘\n║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐\n║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘\n║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐\n║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘\n")
 
elif (kasutajaValik == 3):
hetkekordaja = muster3
print("▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░\n░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄\n▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░\n░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄\n▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░\n░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄\n▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░\n░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄\n")
 
elif (kasutajaValik == 4):
hetkekordaja = muster4
print("░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐\n░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘\n░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐\n░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘\n░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐\n░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘\n░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐░░┌┐\n░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘░░└┘\n")
 
elif (kasutajaValik == 5):
hetkekordaja = muster5
print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n")
 
elif (kasutajaValik == 6):
hetkekordaja = muster6
print("██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄\n▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██\n██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄\n▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██\n██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄\n▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██\n██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄\n▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██▀▄██\n")
 
else:
print("Kasutaja on sisestanud olematu valiku")
summa = põrand*hetkekordaja
 
print("Teie põrand läheb maksma "+str(summa)+" eurot. Kas maksate? (jah/ei)")
kasmaksab = input().lower()
if (kasmaksab == "ei"):
summa *= 0.9
print("Alandasime hinda 10% võrra, summa on nüüd "+str(summa)+" eurot. Kas maksate? (jah/ei)")
kasmaksab = input().lower()
if (kasmaksab =="ei"):
summa *= 0.9
print("Alandasime hinda veel 10% võrra, viimane pakkumine on "+str(summa)+" eurot. Kas see hind sobib? (jah/ei)")
kasmaksab = input().lower()
if (kasmaksab =="ei"):
print("Kahjuks me hinda rohkem alandada ei saa, palun tulge jälle")
else:
print("Palun, siin on teie põrandaplaadid, palun tulge jälle!")
else:
print("Palun, siin on teie põrandaplaadid, palun tulge jälle!")
else:
print("Palun, siin on teie põrandaplaadid, palun tulge jälle!")
 
# kirjuta programm mis
# küsib kasutajalt kas ta soovib osta boilerit
# (selle jaoks on vaja risttahuka valemit kasutada, ning küsida kasutajalt a ja b külg oõhjapindala jaoks sentimeetrites ja olevasoleva ala kõrguse h)
# olenevalt olemasolevast ruumalast
# - kui ruumala on liiga väike, öeldakse et meil ei ole pakkuda midagi sellises suuruses
# - kui ruumala on väike aga sobiv, pakutakse väikest boilerit väikese hinnaga
# - kui ruumala on paras, siis pakutakse väikest boilerit ja parajast boilerit
# - kui ruumala on suur, siis pakutakse väikest, parajast ja suurt boilerit.
# - kasutajalt küsitakse millist boilerit ta osta soovib NIMEPIDI, programm peab tuvastama õige nime kasutades .lower() või .upper() meetodeid
# väikese boileri maht arvutada a=35 b=35 h=70
# paraja boileri maht arvutada a=45 b=45 h=90
# suure boileri maht arvutada a=60 b=60 h=210
# hinnad mõtlete ise välja
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind