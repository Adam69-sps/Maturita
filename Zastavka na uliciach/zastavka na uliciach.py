import tkinter
canvas = tkinter.Canvas(width = 600, height = 600)
canvas.pack()

entry1 = tkinter.Entry()
entry1.pack()

def kresli():
    canvas.delete("all")
    vyska_pred = 0
    with open("zastavba_na_ulici.txt") as subor:
        x = 10
        y = 500
        for riadok in subor:
            info = riadok.split(" ")
            vyska = int(info[1])
            sirka = int(info[0])
            if vyska == 0:
                canvas.create_rectangle(x,y,x+sirka,y, fill = "green", outline="green")
            else:
                canvas.create_rectangle(x,y,x+sirka,y-vyska, fill = "gray")
            if vyska_pred != 0:
                if abs (vyska-vyska_pred) > int(entry1.get()):
                    canvas.create_line(x,y-vyska,x,y-vyska_pred,fill = "red",width = 3)

            x += sirka
            vyska_pred = vyska

button1 = tkinter.Button(text = "kresli", command = kresli)
button1.pack()
                
