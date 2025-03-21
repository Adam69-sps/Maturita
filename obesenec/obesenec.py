from random import *
with open("slovnik.txt") as f:
    slovicka = []
    for riadok in f:
        riadok = riadok.strip()
        slovicka.append(riadok)
        slovo = choice((slovicka))
        slovo_hviezdicky = len(slovo)*"*"
        slovo_hadane = ""
        pokusy = 10
        hra = True
    print("\nHadane slovo: "+slovo_hviezdicky)

    while hra:
        print("Mate "+str(pokusy)+" pokusov")
        hadane = input("Zadaj jedno pismeno: ")

        if len(hadane) != 1:
            print("Iba jedno piseno")
            continue

        if hadane in slovo:
            slovo_hviezdicky = "".join([slovo[i] if slovo[i] in hadane else slovo_hviezdicky[i] for i in range(len(slovo))])
            slovo_hadane += hadane
            print("Hadane slovo: "+slovo_hviezdicky)
            print("Tieto pismena si uz hladal: "+slovo_hadane + " ")

        if hadane not in slovo:
            print("Toto pismeno sa v slove nenachaza")
            slovo_hadane += hadane
            print("Tieto pismena si uz hladal: "+slovo_hadane)

        if pokusy == 0:
            print("prehral si")
            hra = False

        if slovo_hviezdicky == slovo:
            print("Vyhral si")
            hra = False
