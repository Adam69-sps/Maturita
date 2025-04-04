subor = open("dopravny_prieskum.txt", "r")
zastavky = []


def citanie():
    for riadok in subor:
        data = riadok.strip().split()
        if len(data) == 3:
            nastup, vystup, nazov = int(data[0]), int(data[1]), data[2]
            zastavky.append((nastup, vystup, nazov))

    subor.close()


def pocty(zastavky):
    print("Počty cestujúcich po odchode zo zastávky:")
    pocet = 0
    for nastup, vystup, nazov in zastavky:
        pocet += nastup - vystup
        print("{}: {} cestujúcich".format(nazov, pocet))


def odporucany(zastavky):
    maxc = max(sum(i[:2]) for i in zastavky)
    if maxc > 50:
        return "dlhá"
    elif maxc > 20:
        return "štandardná"
    else:
        return "krátka"


def automat(zastavky):
    vhodne = [i[2] for i in zastavky if i[0] >= 10]
    print("Zastávky vhodné na automat:", vhodne)


def zastavky_na_znamenie(zastavky):
    vhodne = [i[2] for i in zastavky if i[0] < 3 and i[1] < 3]
    print("Zastávky na znamenie:", vhodne)


citanie()
pocty(zastavky)
print("Odporúčaný typ električky:", odporucany(zastavky))
automat(zastavky)
zastavky_na_znamenie(zastavky)
