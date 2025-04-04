import random

body = 0
nespravne = []

def generuj():
    global body,nespravne
    with open ("nassobilka.txt", "w") as subor:
        for i in range(10):
            cislo1 = random.randrange(1,100)
            cislo2 = random.randrange(1,100)
            vysledok = cisla1 * cisla2
            print(cislo1,"*", cislo2,"*")

            input1 = int(input("Zadaj vysledok"))
            if input1 == vysledok:
                print("spravne")
                body += 1
            else:
                print("nespravne")
                body += 0
                nespravne.append((i, cislo1, cislo2,vysledok))

            subor.write(f"{cislo1} * {cislo2} = {vysledok}\n")
    subor.close()

def opakuj():
    global nespravne
    for i, cislo1, cislo2, vysledok in nespravne:
        item = i, cislo1,cislo2,vysledok
        print(f"skus to znova priklad {i}:{cislo1} * {cislo2} = ?")

        input2 = int(input(" Zadaj spravny vysledok"))
        if input2 == vysledok:
            print("spravne")
            nespravne.remove(item)
        else:
            print("nespravne")

print("pocet bodov je ", body)
generuj()
opakuj()
