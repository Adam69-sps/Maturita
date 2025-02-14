subor = open("Objednanejedla.txt", "r")

s = {"z":0,"c":0, "h":0, "m":0}
pocet = 0
for riadok in subor:
    info = riadok.split()
    jedlo = info[1]
    pocet += 1
    s[jedlo] = s.get(jedlo, 0) + 1

print("pocet jedál:",pocet)
malo = ""
for jedlo, pocet in s.items():
    print("kod jedla:{} pocet objednavok:{}".format(jedlo,pocet))
    if pocet<20:
        malo = malo + str(jedlo) + ", "
malo = malo [:-2]
if malo != "":
    print("malo objednavok maju tieto jedla:", malo)
else:
    print("vsetky jedla si objednalo aspon 20 ludi")

subor.close()
