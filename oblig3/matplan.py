#Et program lager en ordbok hvor hver nøkkelverdi er navnet
#til en beboer, og innholdsverdien er en liste med tre måltider.
def maltider():
    matlist = {"kari nordmann": ["brød" , "egg", "pølser"],
        "erna solberg": ["yoghurt", "ris", "pizza"],
        "jens stoltenberg": ["melk", "burger", "suppe"],
        "rokas magnus": ["granola", "kylling", "chips"]}
#I en prosedyre brukeren kan skrive navnet til en beboer og da får brukeren
#skrevet ut matplanen til den beboeren.
#hvis beboeren er ikke registrert da brukeren får meldinger "Den beboeren er ikke registrert"
    mat = input("Skriv inn navnet: ")
    mat = mat.lower()
    if mat in matlist:
        print(matlist[mat])
    else:
        print("Den beboeren er ikke registrert")
maltider()
