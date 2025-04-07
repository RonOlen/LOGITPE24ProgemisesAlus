from random import randint

vanus = ""
sunnipaev = ""
sunniaasta = ""
sunnikuu = ""
sugu = ""

isikukood = ""

while(vanus == "" or sunnipaev == "" or sunniaasta == "" or sunnikuu == "" or sugu == ""):
    vanus = input("Palun sisestage oma vanus")
    sunnipaev = input(" Palun sisesta oma sunnipaev")
    sunnikuu = input("Palun sisesta oma sunnikuu nt Jaanuar on 1 jne")
    sunniaasta = input("Palun sisesta oma sünniaasta viimased kaks numbrit")
    if sugu.upper() == "M":
          isikukood += "3"
    elif sugu.upper() == "N":
          isikukood += "4"
    else:
          print("oled sisestanud tundmatu sisestuse, proovi oma sugu uuesti sisestada.")
          sugu = ""
    isikukood += sunniaasta
    if (int(sunnikuu) < 10):
        sunnikuu = "0"+sunnikuu
    isikukood += (sunnikuu + sunnipaev)
    arv = randint(1,9999)
    arvtekstina = ""
    if arv < 10:
        arvtekstina = "000"+str(arv)
    if arv < 100:
        arvtekstina = "00"+str(arv)
    if arv < 1000:
        arvtekstina = "0"+str(arv)
    isikukood += arvtekstina
täisnimi = ""
while (täisnimi == ""):
    täisnimi = input("Kuidas on teie ees ja perekonnanimi").title()

print("Palun",täisnimi,". Siin on teie isikukood ->",isikukood)