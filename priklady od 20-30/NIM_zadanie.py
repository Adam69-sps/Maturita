import tkinter, random
canvas = tkinter.Canvas(width=650, height=200)
canvas.pack()

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')
