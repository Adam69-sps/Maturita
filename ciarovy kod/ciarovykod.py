import tkinter, random
canvas = tkinter.Canvas(width = 200, height = 200)
canvas.pack()

def vykresli_kod(x,y,kod):
    for index in range(len(kod)):
        cislo = kod[index]
        if cislo == 0:
            continue
        posun_y = 60
        if index == 0 or index == len(kod)-1:
            posun_y = 80
        canvas.create_line(index*10 + x, y, index*10 + x, y + posun_y, width = int(cislo))
        canvas.create_text(x + 5*(len(kod)-1), y + 70, text=kod)

def vykresli_4_kody():
    suradnice = ((10,10),(100,10), (100, 100),(10, 100))
    for suradnica in suradnice:
        if len(kody) > 0:
            kod = kody.pop(0)
            vykresli_kod(suradnica[0], suradnica[1], kod)

prvy = True
def medzerink(event):
    global prvy
    if event.keysym == "space":
        canvas.delete("all")
        if prvy:
            vykresli_kod(10, 10, kody.pop(0))
            prvy = False
        else:
            vykresli_4_kody()

with open("slovnik.txt") as subor:
    kody = []
    for riadok in subor:
        if riadok.strip() != "":
            kody.append(riadok.strip())

nahodny_kod = str(random.randint(10000000, 99999999))

vykresli_kod(10,10,nahodny_kod)
canvas.bind_all("<Key>", medzerink)
        
        
