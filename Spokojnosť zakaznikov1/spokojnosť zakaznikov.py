spokojni = [0] * 24
nespokojni = [0] * 24

subor = open("spokojnost_2.txt","r")
for riadok in subor:
    riadok = riadok.strip()
    info = riadok.split()
    spokojnost = info[1]
    cas = info[0].split(":")
    hodina = int(cas[0])
    minuta = int(cas[1])
    if spokojnost == "áno":
        spokojni[hodina] += 1
    else:
        nespokojni[hodina] += 1
pocet_spokojnych = sum(spokojni)
pocet_nespokojnych = sum(nespokojni)
spolu = pocet_spokojnych + pocet_nespokojnych
print("Vyjadrilo sa {} zakaznikov".format(spolu))
pocet_ok = max(spokojni)
hodina = spokojni.index(pocet_ok)
print("Najviac spokojných zák. ({}) je cez hodinu:{}".format(pocet_zle,hodina))

percenta_spokojnosti = [0] * 24
for i in range(24):
    pocet = spokojni[i] + nespokojni[i]
    if pocet > 0:
        if percenta_spokojnosti[i] > 0:
            print("V {}. hodine je spokojnych {:5.2}%".format(i,percenta_spokojnosti[i]))
