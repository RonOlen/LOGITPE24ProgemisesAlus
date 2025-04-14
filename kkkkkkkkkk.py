from random import randint
umbes = randint(1,3)

hapukapsas = ""
pott = ""
vesi = ""
kartul = ""
puljong = ""
kebab = ""

while hapukapsas == "" or pott == "" or vesi == "" or kartul == "" or puljong == "" or kebab == "":
    hapukapsas = input("Kas sul on hapukapsast? (jah/ei): ")
    
    if hapukapsas == "ei":
        print("Saab hautist teha ... kahjuks")
        pott = input("Kas sul on pott madam? (jah/ei): ")
        
        if pott == "ei":
            print("Suppi teha ei saa.")
            break
        
        vesi = input("Kas sul on vett? (jah/ei): ")
        
        if vesi == "ei":
            print("Saab mulgikapsaid teha... kapsas on mid")
            kartul = input("Kas sul on kartulit? (jah/ei): ")
            if kartul == "ei":
                print("Ilma kartulita ei tee midagi.")
                break
                
            puljong = input("Kas sul on puljongit? (jah/ei): ")
            if puljong == "ei":
                print("Ilma puljongita ei tee midagi.")
                break
            
            kebab = input("Kas sul on midagi muud kapis? (jah/ei): ")
            if kebab == "jah":
                print("Siis saame teha ühepäevatoitu, yipee!")
            elif kebab == "ei":
                print("Sa saad süüa hapukapsast.")
                
        elif vesi == "jah":
            print("Supp on võimalik teha, lasen edasi küsida.")
        
    elif hapukapsas == "jah":
        print("Hapukapsas on olemas!")
        pott = input("Kas sul on pott madam? (jah/ei): ")
        
        if pott == "jah":
            vesi = input("Kas sul on vett? (jah/ei): ")
            if vesi == "jah":
                kartul = input("Kas sul on kartulit? (jah/ei): ")
                if kartul == "jah":
                    puljong = input("Kas sul on puljongit? (jah/ei): ")
                    if puljong == "jah":
                        kebab = input("Kas sul on midagu muud kapis? (jah/ei): ")
                        if kebab == "jah":
                            print("Siis saame teha ühepajatoitu!")
                        if kebab == "ei" and umbes == 1:
                            print("saab ka süüa hautist.")
                        if kebab == "ei" and umbes == 2:
                            print (" Saad teha mulgikapsaid")
                        if kebab == "ei" and umbes == 3:
                            print ("Saad teha suppi")
                    else:
                        print("Ilma puljongita ei saa teha.")
                        break
                else:
                    print("Ilma kartulita ei saa teha.")
                    break
            else:
                print("Ilma veeta ei saa midagi teha.")
                break
        else:
            print("Potti ei ole, siis midagi teha ei saa.")
            break