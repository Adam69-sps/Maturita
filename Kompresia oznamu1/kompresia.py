veta = str(input("Zadaj vetu:"))
zoz = veta.split()
kompresia = []

pocet_slov = len(veta)
print(pocet_slov)

stlacene = ""
for i in zoz:
    stlacene+=str(i)
print(stlacene)

for i in range(len(zoz)):
    if i%2==0:
        kompresia.append(zoz[i].upper())
    else:
        kompresia.append(zoz[i].lower())

vystup = ""
for i in kompresia:
    vystup+=str(i)
print(kompresia)
