subor = open("hada.txt","r")
subor2 = open("kompresia.txt","w")

def kompresia(s):
    if s== "":
        return ""
    pismeno=s[0]
    pocet = 0
    vystup= ""
    for znak in s:
        if znak == pismeno:
            pocet+=1
        else:
            vystup = vystup + "{} {}".format(pismeno,pocet)
            pismeno = znak
            pocet = 1
    vystup = vystup + "{} {}".format(pismeno,pocet)
    return vystup

riadky= list(subor)
print(riadky)
print("Pocet riadkov v subore"),len(riadky)
dlzky=[]
for riadok in riadky:
    riadok=riadok.strip()
    dlzky.append(len(riadok))
    print(kompresia(riadok), file =subor2)
print("Pocet krokov najdlhsej hre:",max(dlzky))
subor.close()
subor2.close()


    
