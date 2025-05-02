#fail = open("andmed.txt", encoding = "UTF-8") #omistame faili ühte muutujasse
#kokkujoostud = 0
#for rida in fail: #for tsükliga kuvame faili read ukshaaval valja
#    kokkujoostud += float(rida)
#fail.close() # sulgume faili
#print("Sul on kokku joostud "+str(kokkujoostud)+"kilomeetrit")

#lisa juurde for tsükkel, mis filteerib välja kõik jooksmised
# kus on joostud rohkem kui 10 km
#fail = open("andmed.txt", encoding = "UTF-8") #omistame faili ühte muutujasse meetodiga op
#for rida in fail:
#    if float(rida) >= 10.0
#    print(rida.strip())
    
#fail.close() #sulgume faili

# kuva välja jooksude kogusumma järjendi abil

# kuva välja kõik jooksud mis on 10km või vähem

# arvuta välja keskmine joostud vahemaa jooksukorra kohta

#fail = open("andmed.txt", encoding = "UTF-8") #omistame faili ühte muutujasse
#kokkujoostud = 0
#failcontent = []
#for rida in fail: #for tsükliga kuvame faili read ukshaaval valja
#    failcontent.append(rida.strip())
#fail.close()

for arv in failcontent:
    kokkujoostud += float(arv)
print(kokkujoostud)

# kuva välja kõik jooksud mis on 10km või vähem

# arvuta välja keskmise joostud vahemaa jooksukorra kohta

fail = open("andmed.txt", encoding = "UTF-8") #omistame faili ühte muutujasse meetodiga op
for rida in fail:
    if float(rida) <= 10.0
    print(rida.strip())