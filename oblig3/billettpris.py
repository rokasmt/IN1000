#Problemet er at if-løkka kjører fra toppen og ned, og hvis alderen er over 17
#vil programmet stoppe og sjekker ikke videre.
def billett():
    a = 30
    b = 50
    c = 35
#Et program ber brukeren å skrive inn alderen sin
    alder = int(input("Skriv inn din alder: "))
#Et program sjekker hvis brukeren er under eller akkurat 17 år gammel,
#eller hvis brukeren er over 17 år, men også over 63 år vil den skriv ut billettpris for over 17 år og ikke går videre til neste linje.
    if alder <= 17:
        print(a, "Kr." + " " + "Det er barnebillett")
    elif alder > 17:
        print(b, "Kr." + " " + "Det er vanlig billett")
    elif alder <= 63:
        print(c, "Kr." + " " + "Det er pensjonistbillett")
#prosedyren repeteres 4 ganger
billett()
billett()
billett()
billett()
