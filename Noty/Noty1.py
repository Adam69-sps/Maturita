import tkinter
canvas = tkinter.Canvas(width=1000,height=1000)
canvas.pack()

SIRKA = 400
stupnica = "cdefgah"

def osnova(x,y,dlzka):
    for i in range(5):
        canvas.create_line(x,y+i*10,x+dlzka,y+i*10)
        
def nacitaj_noty(nazov_suboru):
    subor=open(nazov_suboru,"r")
    return subor.readline().strip()

def kresli_notu(x,y):
    canvas.create_oval(x-5,y-3,x+5,y+3)

def vyska(nota):
    return stupnica.find(nota) * 5

def kresli(noty):
    notax = 20
    osnovay = 10
    osnova(0, osnovay, SIRKA)
    pocet = 0
    for nota in noty:
        kresli_notu(notax, osnovay+5*10 - vyska(nota))
        notax +=20
        pocet +=1
        if pocet+1 == SIRKA // 20:
            osnovay += 100
            notax = 20
            pocet = 0
            osnova(0,osnovay,SIRKA)

noty = nacitaj_noty("Noty.txt")
kresli(noty)
