 #kirjuta programm mis
#
# küsib kasutajalt kas tal on kõht tühi.
# kui kasutaja vastab ei:
#---siis programm ütleb talle vastu tagasi "ootame teid jälle kui teil isu on"
# kui kasutaja vastab ja:
#---küsib programm kas ta tahab ise võileiva kokku panna, või lasta arvutil selle genereerida
#---kui kasutaja tahab ise kokku panna, siis:
#-------küsib programm temalt kas ta tahab ühepoolset võileiba või kahepoolset võileiba:
#-------küsib programm temalt kas ta tahab võileivale võid või majoneesi
#-------küsib programm temalt kas ta tahab kurki võileivale
#-------küsib programm temalt kas ta tahab tomatit võileivale
#-------küsib programm temalt kas ta tahab peekonit võileivale
#---kui kasutaja tahab suvaliselt kokku panna, siis genereeritakse talle 5 korda erinev võileiva osa järjest
#---programm koostab kasutajale ascii pildi erinevatest kihtidest mida kasutaja lisanud on või arvuti genereerinud on
#---, ja küsib temalt raha 1.50 + 0.75 iga lisatud kihi eest
#---kui kasutaja ei maksa, siis öeldakse talle "ootame teid jälle kui teil isu on ja raha ka"
#---kui kasutaja maksab, siis tagastatakse ascii võileib teatega "aitäh tellimuse eest, tulge jälle"
# sai - [ , ,, '' ']
# või ja majoneesi jaoks ei kuvata kihti, aga ta annab hinnas lihtsalt juurde
# kurk - ▄▄▄▄ ▄▄▄
#tomat - ( | ▌|██)
#bacon - "~-,._.,-~"~-,.

algsumma = 1.50
lisand = 0.75
 
k6htTyhi = input("Kas sul on kõht tühi?")
if (k6htTyhi == "ei"):
    print("Ootame teid jälle kui teil isu on")
else:
    kasutajaValik = input("Kas tahad ise valida komponendid, või lased masinal ise välja mõelda? (ise/masin)")
if (kasutajaValik.lower() == "ise"):
#mingid küsimised
    print("Küsime sinult võileiva kohta mõned küsimused:")
sai = input("Kas tahad ühepoolset või kahepoolset võileiba? (üks/kaks)")
kaste = input("Kas tahad võid või majoneesi? (või/majo)")
kurk = input("Kas tahad võileivale värsket kurki? (jah/ei)")
tomat = input("Kas tahad võileivale värsket tomatit? (jah/ei)")
peekon = input("Kas tahad võileivale krõbedat peekonit? (jah/ei)")
if (kasutajaValik.lower() == "masin"):
    print("Palun oota kuni võileivaautomaat genereerib sulle võileiva")
saiRand = randint(0,1)
kasteRand = randint(0,1)
kurkRand = randint(0,1)
tomatRand = randint(0,1)
peekonRand = randint(0,1)
if bool(saiRand) == True:
    sai = "kaks"
else:
    sai= "üks"
if bool(kasteRand) == True:
    kaste = "majo"
else:
    kaste = "või"
if bool(kurkRand) == True:
    kurk = "jah"
else:
    kurk = "ei"
if bool(tomatRand) == True:
    tomat = "jah"
else:
    tomat = "ei"
if bool(peekonRand) == True:
    peekon = "jah"
else:
    peekon = "ei"
if (sai == "kaks"):
    algsumma += lisand
    print("[ , ,, '' ']")
 
if (kaste == "majo"):
    algsumma += lisand
if (kurk == "jah"):
    algsumma += lisand
    print(" ▄▄▄▄ ▄▄▄")
if (tomat == "jah"):
    algsumma += lisand
    print(" ( | ▌|██)")
if (peekon == "jah"):
    algsumma += lisand
    print('"~-,._.,-~"~-,.')
if (sai == "üks"):
    print("[ , ,, '' ']")
    print("\n siin on teie võileib, see teeb: "+str(algsumma)+" €.")    
        