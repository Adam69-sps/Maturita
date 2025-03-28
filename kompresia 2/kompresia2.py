def stlac_text(text):
    novy_text = ""
    for slovo in text.split():
        novy_text+=slovo.capitalize()
    return novy_text


def odtlac_text(text):
    novy_text = ""
    for pismeno in text:
        if ord(pismeno) in range(ord("A"), ord("Z")+1):
            novy_text += " "
        novy_text+=pismeno.upper()
        return novy_text.strip()

oznam = input("zadaj vetu: ")
print("Pocet slov vo vete: ", len(oznam.split()))
print(stlac_text(oznam))
print(odtlac_text(stlac_text(oznam)))
