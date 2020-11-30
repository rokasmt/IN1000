from person import Person

def hovedprogram():

    person = Person(input("Navn: "), int(input("Alder: ")))

    leggHobby = input("Legg til hobby, trykk y for å stoppe!")

    while leggHobby != "y":
        leggHobby = input("Legg til hobby, trykk y for å stoppe!")
        person.leggTilHobby(leggHobby)
    person.skrivUt()

hovedprogram()
