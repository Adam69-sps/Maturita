slova = []
anglicke = []
slovenske = []
chyby = 0

with open("ucenie.txt","r", encoding="utf-8") as subor:
    for i in subor:
        slova.append(i.strip())

for i in range(len(slova)//2):
    anglicke.append(slova[i*2])
    slovenske.append(slova[i*2 +1])

otazka = ""

while not otazka in ("slovenske","anglicke"):
    otazka = str(input("Zadaj slovenske alebo anglicke:"))
    if otazka=="anglicke":
        anglicke, slovenske = slovenske, anglicke
    else:
        pass
    
while anglicke!=[]:
    print(anglicke[0])
    pokus = str(input("zadaj prelozene slovo:"))
    if pokus == slovenske[0]:
        anglicke.pop(0)
        slovenske.pop(0)
        print("spravne")
        print(chyby)
    else:
        anglicke.append(anglicke[0])
        slovenske.append(slovenske[0])
        anglicke.pop(0)
        slovenske.pop(0)
        print("skus znovu")
        print(chyby)
