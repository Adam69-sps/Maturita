import tkinter as tk

grid_size = 10
cell_size = 40

canvas = tk.Canvas(width = grid_size * cell_size, height = grid_size, bg = "white")
canvas.pack()

farba_entry = tk.Entry()
farba_entry.pack()
farba_entry.insert(0, "#000000")

mapa = [["#FFFFFF" for _ in range(grid_size)] for _ in range(grid_size)]

def nakresli_mriezku():
    for i in range(grid_size):
        for j in range(grid_size):
            x1,y1  = i * cell_size, j * cell_size
            x2,y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1,y,x2,y2, outline = "black", fill = mapa[i][j])

def vyfarbi_policko(event):
    x,y = event.x // cell_size, event.y // cell_size
    farba = farba_entry.get()
    mapa[y][x] = farba
    canvas.create_rectangle(x * cell_size, y * cell_size,(x + 1) * cell_size, (y +1) * cell_size, outline = "black", fill = farba)

def uloz_mapu():
    nazov_suborou = "editor_leveov_vystup1.txt"
    with open(nazov_suboru, "w") as subor:
        for riadok in mapa:
            subor.write(" ".join(riadok) + "\n")
    print(f"mapa bola ulozena do {nazov_suboru}")

ulozit_button = tk.Button(text = "Uložiť", command = uloz_mapu)
ulozit_button.pack()

canvas.bind("<Button-1>", vyfarbi_policko)
nakresli_mriezku()
canvas.mainloop()
