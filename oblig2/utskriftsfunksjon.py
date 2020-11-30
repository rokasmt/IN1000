#Et program komuniserer med en bruker. Brukeren tar inn et navn og et bosted fra terminalen.
#Prosedyren repeteres 3 ganger og derfor faar vi informasjon om 3 personer.
def navnsted():
    navn = input("Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")
    print ("Hei, " + navn + "! " "Du er fra " + sted + "." '\n')
navnsted()
navnsted()
navnsted()
