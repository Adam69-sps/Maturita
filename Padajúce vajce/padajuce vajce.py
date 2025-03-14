import tkinter, random
canvas = tkinter.Canvas(width = 800, height = 800)
canvas.pack()

def nove_vajicko():
    global pismeno, x, y, skryte
    pismeno = chr(random.randint(ord("a"), ord("z")))
    x = random.randint(1, 790)
    y = 0
    skryte = True

def cyklus():
    global y, skryte
    canvas.delete("all")

    y += 8
    if (y >= 2/3 * 500):
        skryte = False
        
    canvas.create_oval(x - 10, y - 20, x + 10, y + 20)
    if not (skryte):
        canvas.create_text(x,y,text = pismeno)
        
    canvas.update()
    if not (y >= 500):
        canvas.after(100, cyklus)

def klavesnica(event):
    klavesa = event.keysym
    if klavesa == pismeno:
        nove_vajicko()
canvas.bind_all("<Key>", klavesnica)

nove_vajicko()
cyklus()
        

