import random
subor1 = open("poprehadzovany_text1_vstup.txt", "r")
subor2 = open("poprehadzovany_text1_vystup.txt", "w")

for riadok in subor1:
    print(riadok, end= "")
    slova = riadok.stip().split()
    for i in range(len(slova)):
        slovo = slova[i]
        pismenka = list (slovo[1:-1])
        random.shuffle(pismenka)
        slova[i] = slovo[0] + ' '.join(pismenka) + slovo[-1]
    riadok = ''
    for slovo in slava:
        riadok += slovo +' '
    riadok = riadok[:-1] + '\n'
    print(riadok, end="")
    subor2.write(riadok)
subor1.close()
subor2.close()
