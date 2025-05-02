# kirjuta program mis
# loeb failist laulusõnu (ise valid laulu)
# kuvab välja kõik sõnad
# arvutab kokku mitu täishäälikut on (aeiouõäöüy)
# kuvab välja kõik sõnad mis on pikemad kui 7 tähte
# laseb kasutajal kirjutada ise ühe värsi (4 rida)

tähed = "aeiouõäöüy"

failinimi = input("Sisesta failinimi, kust laulusõnu lugeda: ")

täht = []
with open(failinimi, 'r', encoding='utf-8') as file:
    sisu = file.read()
    täht = sisu.split()

if len(täht) == 0:
    print("Failis pole sõnu!")
else:
    print("\nKõik sõnad laulusõnades:")
    print(" ".join(täht))
    
    täishäälikud = 0
    for word in täht:
        for el in word.lower():
            if el in tähed:
                täishäälikud += 1
    print(f"\nLaulusõnades on kokku {täishäälikud} täishäälikut")
    
    print("Siin on sõnad, mis on pikemad kui 7 tähte:")
    for word in täht:
        if len(word) > 7:
            print(word)
    
    print("\nPalun kirjuta üks värss (4 rida):")
    värss = []
    i = 1
    while i <= 4:
        line = input(f"Rida {i}: ")
        värss.append(line)
        i += 1
    
    print("\nSinu kirjutatud värss:")
    for line in värss:
        print(line)