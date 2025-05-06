# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# kirjuta programm mis
#
# küsib kasutajalt kas tal on perekonnaliikmeid
# - kui jah, siis küsib nende kõikide liikmete lemmikloomanimesid
# - kui ei, siis küsib kas kasutajal on lemmikloomi
# - - kui jah, siis küsib kõiki nimesid
# - - kui ei, siis ütleb kahju, pesaleidjas on palju kasse kes tahaksid kodu.
# programm väljastab lause, kus loetletakse kõik lemmikloomad, lemmikloomade puudumisel seda sammu ei tehta
pereliikmed = ""
lemmikloomaarv = ""
kasonloom = ""

while pereliikmed =="":
    pereliikmed = input("Kas sul on pereliikemid? jah/ei")
    if pereliikmed == "jah":
        print("\nÜtle oma lemmikloomanimed")
        lemmikloomaarv = []
        
        line = input(": ")
        line2 = input(": ")

        lemmikloomaarv.append(line)
        lemmikloomaarv.append(line2)

            
            
        print("\nSinu lemmik loomade nimed on:")
        for line in lemmikloomaarv:
            print(line)
            
    if pereliikmed == "ei":
        kasonloom = input(" Aga kas sul on lemmikloomi? jah/ei")
        if kasonloom == "jah":
            print("\nÜtle oma lemmikloomanimed")
            lemmikloomaarv = []
        
            line = input(": ")
            lemmikloomaarv.append(line)
            
            
            print("\nSinu lemmik loomade nimed on:")
            for line in lemmikloomaarv:
                print(line)
            if kasonloom == "ei":
                print("kahju, pesaleidjas on palju kasse kes tahaksid kodu.")
        
    

    