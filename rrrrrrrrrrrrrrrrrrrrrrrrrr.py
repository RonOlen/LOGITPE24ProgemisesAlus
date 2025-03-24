from random import randint # võtame sisse randint() funktsiooni random paketist
 
eludeArv = 3 # mängijal olevad elud
kristalle = 0 # mängijal olevad kristallid
raha = 5 # mängija rahakotis olev raha
haldjaidAidatud = 0 # mitu korda mängija on haldjaid aidanud
mängLäbi = False
 
while (eludeArv > 0 or mängLäbi == False ): # mängu põhitsükkel, toimib niikaua kuni elusi on rohkem kui 0
### juhtum 1, redel
    print("Astusid redeli alt läbi, ning nägid ", end = "") # end siin ei vaheta rida, kuna endi parameeter on tühi sõne
võimalikTulevik = randint(1,3) # tekitame juhuarvu, et anda kasutajale üks kolmest võimalikust sündmusest
if võimalikTulevik == 1: # sündmus 1, must kass
    print("musta kassi.")
    eludeArv -= 1
    print("Su süda tegi suure jõnksu ja tundus nagu sa oleks kaotanud terve ühe elu.")
elif 	võimalikTulevik == 2: # sündmus 2, tablett
        print(" maas mingisugust tabletikest. Sellel on peal pikachu pilt.")
        selleSündmuseTulevik = randint(1,2)
        if selleSündmuseTulevik == 1:
        print("Otsustasid maitsta mis maitsega on, oli hea, aga kahjuks kaotasid kõik elud")
eludeArv -= eludeArv
else:
    print("Maast üles võttes, lagunes tablett kahjuks tolmuks. Pühkisid käed puhtaks ja läksid edasi")
else:
    print("et sinu auto juures seisab politseinik. \n Nägu on tal üsna punane, ning selgelt näost näha põlevat viha.")
    print("Politseinik ütleb kasutajale: 'Teie auto on pargitud kõnniteele liiga lähedale! Kas liigutate oma autot?'")
    kasutajaVastusPolitseinikule = ""
    while (kasutajaVastusPolitseinikule == ""):
    kasutajaVastusPolitseinikule = input().lower()
    if kasutajaVastusPolitseinikule == "jah":
    print("Viisid oma auto teise kohta, leidsid asfaldilt autost väljatulles maast ühe raha.")
raha += 1
elif kasutajaVastusPolitseinikule == "ei":
    print("MISMÕTTES EI, TE OLETE PARGITUD VALESTI, SAATE TRAHVI!!!!!!1!1one.")
    print("Said trahvi 20 raha.")
raha -= 20
else:
kasutajaVastusPolitseinikule = ""
###
    print("Sinu hetkeseis on: \n elusid = "+str(eludeArv)+"\n raha = "+str(raha)+"\n kristalle = "+str(eludeArv))
    print("Vajuta enter et jätkata")
input()
if eludeArv == 0:
mängLäbi = True
break
### juhtum 2, veider objekt
print("Kõndisid tänaval edasi ja nägid veidrat objekti. ", end = "") # end siin ei vaheta rida, kuna endi parameeter on tühi sõne
võimalikTulevik = randint(1,3) # tekitame juhuarvu, et anda kasutajale üks kolmest võimalikust sündmusest
if võimalikTulevik == 1: # sündmus 1, pisike lendav taldrik
    print("See nägi välja nagu lendav taldrik, aga imepisike.")
    print("Sa vaatasid seda natuke, kui järsku muutus käeshoitav lendav taldrik, kristalliks.")
    print("Said ühe kristalli.")
kristalle += 1
elif võimalikTulevik == 2: # sündmus 2, hambahari
print("Lähemale minnes avastasid, et keegi on hambaharja sõlme keeranud.")
selleSündmuseTulevik = randint(1,2)
if selleSündmuseTulevik == 1:
    print("Sa ei teadnud mida sellega teha ja otsustasid nuusutada seda.")
    print("Kohutav lehk võttis sult ühe elu.")
eludeArv -= 1
else:
    print("Otsustasid visata selle sõiduteele, parasjagu sõitis teel Elon Musk, ja")
    print("ta isejuhtiv auto ei osanud midagi teha, sõitis üle ja keeras auto vasta seina")
    print("Elon suri ja sina said tema rahakotis oleva raha endale. Tüüp oli parm, ainult 5 raha oli tal")
raha += 5
else:
if(kristalle >19):
    print("Kasutaja ette ilmus haldjas. Haldjas ütles kasutajale: 'Meil on abi vaja!'")
    print("'Me kasutame kristalle inimeste vähi ravimiseks, kas sa loovutad meile 5 kristalli?'")
kasutajaHaldjaOtsus = ""
while (kasutajaHaldjaOtsus == ""):
kasutajaHaldjaOtsus = input().lower()
if kasutajaHaldjaOtsus == "jah":
    print("Otsustasid haldjaid aidata, kaotasid küll 5 kristalli, aga said terve kuhja head tuju.")
kristalle -= 5
haldjaidAidatud +=1
if haldjaidAidatud == 3:
    print("'Oled meid palju aidanud, tule meie külla, kohtleme sind kui kangelast oma lahke abi eest.'")
    print("Oled Võitnud, Mäng Läbi")
mängLäbi == True
elif kasutajaRahakotiOtsus == "ei":
    print("'Selge rändur, kuni järgmise korrani.'")
else:
kasutajaRahakotiOtsus = ""
else:
    print("See oli musta värvi lapik ristkülik")
    print("Ees kõnnib mees, kes ilmselgelt pillas oma rahakoti maha.")
    print("Kas sa tagastad rahakoti sellele mehele?")
kasutajaRahakotiOtsus = ""
while (kasutajaRahakotiOtsus == ""):
kasutajaRahakotiOtsus = input().lower()
if kasutajaRahakotiOtsus == "jah":
    print("Otsustasid rahakoti tagastada, mees tänas ja andis imeliku kivikese.")
    print("See oli kristall, sa said ühe kristalli juurde.")
kristalle += 1
elif kasutajaRahakotiOtsus == "ei":
    print("Rahakotis oli ainult 10 raha.")
raha += 10
else:
kasutajaRahakotiOtsus = ""
###
    print("Sinu hetkeseis on: \n elusid = "+str(eludeArv)+"\n raha = "+str(raha)+"\n kristalle = "+str(eludeArv))
    print("Vajuta enter et jätkata")
    input()
if eludeArv == 0:
mängLäbi = True
break
 
if eludeArv == 0:
    print("Mängläbi, kaotasid kõik")