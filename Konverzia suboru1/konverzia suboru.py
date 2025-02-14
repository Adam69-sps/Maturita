def spracuj_riadok(vstup):
    pocet = len(vstup) //2
    vstup = ""
    for i in range(pocet):
        odtien = vstup[i*2:i*2+2]
        farba = "0"
        if odtien > "7f":
            farba = "1"
        vystup += farba + " "
    vystup = vystup [:-1] + "\n"
    return vystup

subor = open("ciernobiely_obrazok_1.txt","r")
subor_out = open("konverzia_suboru_1_vystup.txt","w")
riadok = subor.readline()
velkost = riadok.split()
subor_out.write(riadok)
sirka = int(velkost[0])
vyska = int(velkost[1])
print("obrázok ma rozmery {}x{} bodov".format(sirka, vyska))
print("v obrazku je {} bodov".format(sirka * vyska))
riadok = subor.readline()
print(repr(riadok))
spracovane = spracuj_riadok(riadok)
print(repr(spracovane))
for riadok in subor:
    subor_out.write(spracuj_riadok(riadok))
subor.close()
subor_out.close()
