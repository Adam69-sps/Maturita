import tkinter
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

def stvorceky():
    global x,y
    canvas.create_rectangle(10,100,100,10, fill = "red")
    canvas.create_rectangle(200,100,110,10, fill = "green")
    canvas.create_rectangle(300,100,210,10, fill = "blue")
    canvas.create_rectangle(400,100,310,10, fill = "orange")


def kliknutie(sur):
    if y < sur.y < y + vel:
        poradie = (sur.x - x) // vel
        if 0 <= poradie < len(farby):
            print(poradie)
            student = entry1.get()
            if student != "":
                subor = open("vydaj_jedla.txt","a")
                subor.write(student+" "+skratky[poradie]+"\n")
                subor.close()


canvas.create_text(210, 200, text="VYBER JEDLA!", font="Arial 20", fill = "red")
subor = open("vyber_jedla.txt","w")
farby = ["red","green","blue","orange"]
subor.close()
skratky = "zcmo"
x,y, vel = 10, 40, 100
canvas.bind("<Button-1>", kliknutie)
label1 = tkinter.Label(text="kód študenta:")
label1.pack()
stvorceky()
entry1 = tkinter.Entry()
entry1.pack()
