import tkinter

def nacitaj_subor():
    with open("anketa.txt", encoding = "utf-8") as subor:
        otazka = subor.readline()
        odpovede = []
        for odpoved in subor.readline().split():
            odpovede.append(int(odpoved))
    return otazka, odpovede

def vykresli_anketu(otazka, odpovede):
    canvas.delete("all")
    celkovo_pocet_odpovedi = sum(odpovede)
    slovne_odpovede = ("áno", "nie", "neviem")
    canvas.create_text(10,10, anchor = "nw", text=otazka)
    for i in range(len(odpovede)):
        slovne_odpovede[i]
        canvas.create_text(10,55+ i * 50, anchor = "nw",
                           text="{}. {} - {}".format(i+1, slovne_odpovede[i], odpoved))

        percento = odpoved/celkovy_pocet_odpovedi
        farba = "red"
        if odpoved == max(odpovede):
            farba = "green"
        canvas.create_rectangle(100,50 + i * 50,
                                100+150*percento, i * 50 + 75,
                                fill = farba)

def klavesa(event):
    klavesa = int(event.keysym)
    otazka, odpovede = nacitaj_subor()
    if klaves in range(1, 4):
        odpovede[klaves-1] += 1
        vykresli_anketu(otazka, odpovede)
        for i in range(len(odpovede)):
            odpovede[i] = str(odpovede[i])
        upravene_odpovede = " ".join(odpovede)
        with open("anketa.txt","w", encoding="utf-8") as subor:
            subor.write(otazka)
            subor.write(upravene_odpovede)

canvas = tkinter.Canvas(width = 360, height = 180)
canvas.pack()

otazka, odpovede = nacitaj_subor()
vykresli_anketu(otazka, odpovede)

canvas.bind_all("<Key>", klavesa)
