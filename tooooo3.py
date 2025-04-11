




loom = ""
misloom = ""
kass = ""
koer = ""
dogname = ""
tõug = ""
konsool = ""
knimi=""
while(knimi==""):
    knimi = input("Sisestama ees ja perekonnanimi").title()
    kasonloom = ""
    millineloomaliik = ""
while (millineloomaliik == ""):

    while (loom == "" or misloom == "" or kass == "" or koer == "" or konsool == ""):
        loom = input("Kas teil on lemmikloom? jah/ei")
        if (loom == "jah"):
            misloom = input("kas teil on kass või koer")
        if (misloom == "kass"):
            kass = int(input("Mitu kassi teil on?"))
            kassidenimed = ""
            while kass > 0:
                kassidenimed += input(" Mis on teie kasside nimed üks haaval  ")
                kassidenimed += ", "
                kass -= 1
                print (" Olen kindel, et ",kassidenimed," on väga armas")
        elif (misloom == "koer"):
            tõug = input(" Mis tõug on teie koer?")
            while (koer == ""):
                    dogname = input("Mis on teie koera nimi?")
                    print (" Olen kindel, et teie koer",dogname,"on kena, kuna ta on",tõug,)
        elif (loom == "ei"):
            konsool = input(" Kas teil on konsoole?")
            if (konsool == "jah"):
                konsooltk = int(input(" Mitu konsooli teil on"))
            if (konstooltk >= 3):
                    print (" go touch grass")
            elif (konsool == "ei"):
                    print ("Head aega")