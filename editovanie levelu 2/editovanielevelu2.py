import tkinter as tk

grid_size = 10
cell_size = 40
window_size = grid_size * cell_size

c = tk.Canvas(height = window_size, width = window_size)
c.pack()

prvy_bod = None
steny = set()

def zisti_bundku(event):
    riadok = event.y // cell_size
    stlpec = event.x // cell_size
    return riadok.stlpec

def vypln_bunky(c,zaciatok, koniec):
    global steny
    r1, s1 = zaciatok
    r2, s2 = koniec

    if r1 == r2 or s1 == s2:
        min_r, max_r = sorted([r1, r2])
        min_s, max_s = sorted([s1, s2])
        for r in range(min_r, max_r + 1):
            for s in range(min_s, max_s + 1):
                bunka = (r, s)
                x1, y1 = s * cell_size, r * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                if bunka in steny:
                    steny.remove(bunka)
                    c.create_rectangle(x1,y1,x2,y2, fill = "white", outline = "black")
                else:
                    steny.add(bunka)
                    c.create_rectangle(x1,y1,x2,y2, fill = "blue", outline = "black")

def on_click(event):
    global prvy_bod
    bunka = zisti_bunku(event)

    if prvy_bod is None:
        prvy_bod = bunka
    else:
        vypln_bunky(c, prvy_bod, bunka)
        prvy_bod is None

for i in range(grid_size + 1):
    c.create_line(0, i * cell_size,window_size,i*cell_size, fill = "black")
    c.create_line(i * cell_size, 0, i*cell_size, window_size, fill = "black")

c.bind("<Button-1>",on_click)
