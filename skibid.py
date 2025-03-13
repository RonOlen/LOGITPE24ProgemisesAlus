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

print ("Kas soovide osta broilerit ja/ei ")
vastus = input()
if (vastus == "ja"):
    print (" Mis võiks olla broileri alus?")
    alus1 = int(input())
    print (" Mis on broileri küljealus ?")
    alus2 = int(input())
    print (" Mis on broileri pikkus?")
    pikkus = int(input())


mata = alus1 * alus2 * pikkus

Smallb = 35 * 35 * 70
Medb = 45 * 45 * 90
Bigb = 60 * 60 * 210

Smal = 1000
Bigg = 2500
Largee = 4000

if (mata < Smallb):
    print("Nii väikest ei ole")
elif (mata < Medb):
    print ("Meil on võimalik pakkuda väiksemaid broilereid")
elif (mata < Bigb):
    print (" Suuremaid pole")
else:    
    print ("pakun kõike Millist soovide")
    soov = input()
    
    if (soov == "väike"):
        print (" Toshiba maksab 1000")
        sigma = input(" Kas olete valmis maksma ja/ei ")
    if (sigma == "ja"):
        print ("Täname teid ostu eest!")
    else:
        print ("Pakume soodushinda", Smal * 0.9)
        print ("Kas sobib ? ja/ei")
        vastus3 = intput()
    if (vastus3 == ja):
        print("Täname ostu eest")
    else:
        print(" Pakume välja parema hinna", Smal * 0.75)
        
    if (soov == "keskmine"):
        print (" Samsungi oma maksab 2500")
        sigma = input(" Kas olete valmis maksma ja/ei ")
    if (sigma == "ja"):
        print ("Täname teid ostu eest!")
    else:
        print (" Begone you")
        
    if (soov == "suur"):
        print (" Philips oma maksab 4000")
        sigma = input(" Kas olete valmis maksma ja/ei ")
    if (sigma == "ja"):
        print ("Täname teid ostu eest!")
    else:
        print (" Begone you")
    