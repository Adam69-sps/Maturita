import tkinter
canvas = tktinter.Canvas(width = 800, height = 800)
canvas.pack()


def histogram(hodnoty,mierka):
    for i in range(256):
        canvas.create_rectangle(i*2,500,i*2+2,500-hodnoty[i]/mierka,width=0,fill="grey")

        
        


subor = open("ciernobiely_obrazok_1.txt","r")
riadok = subor.readline()
velkost = riadok.split()
subor_out.write(riadok)
sirka = int(velkost[0])
vyska = int(velkost[1])
print("obrázok ma rozmery {}x{} bodov".format(sirka, vyska))
print("v obrazku je {} bodov".format(sirka * vyska))

odtiene = [0] *256
for riadok in subor:
    for i in range(sirka):
        farba = riadok[i*2:i*2+2]
        dec_farba = int(farba, 16)
        odtiene[dec_farba] +=1
subor.close()
max_vyskyt = max(odtiene)
mierka = (max_vyskyt // 500) +1
print("Najvyšší počet vyskytov odtiena je:",max_vyskyt)
print(odtiene)
histogram(odtiene, mierka)
