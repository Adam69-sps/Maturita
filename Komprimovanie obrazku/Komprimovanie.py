def spracuj_riadok(vstup):
    vstup = vstup.strip()
    dlzka = len(vstup)
    vystup = ""
    if vstup[0] == "1":
        vystup += "0 "
    pocet, i = 0, 0
    spracovavam = vstup[0]
    for znak in vstup:
        if znak == spracovavam:
            pocet += 1
        else:
            vystup += str(pocet) + " "
            spracovavam = znak
            pocet = 1
        vystup +=str(pocet)+ " "
        return vystup[: - 1] +"\n"

subor = open("subory/kompresia_obrazka1.txt","r")
subor_out = open ("subory/kompresia_obrazka_vystup.txt","w")
riadok = subor.readline()
velkost = riadok.split()
subor_out.write(riadok)
sirka = int(velkost[0])
vyska = int(velkost[1])
print("Obrazok ma rozmery {}x{} bodov".format(sirka, vyska))
print("V obrazku ke {} bodov".format(sirka * vyska))
riadok = subor.readline()
print(repr(riadok))
spracovane = spracuj_riadok(riadok)
print(repr(spracovane))
subor_out.write(spracovane)
for riadok in subor:
    subor_out.write(spracij_riadok(riadok))
subor.close()
subor_out.close()

