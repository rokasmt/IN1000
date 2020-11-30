#En funksjon som tar imot to strenger, slår dem sammen og returnere
#den sammenslaate verdien
def slaaSammen(a,b):
    return (a+b)

#En prosedyre som tar imot en liste og skriver ut hvert element
#i liste på hver sin linje ved hjelp av en for-løkke
def skrivUt(liste):
    for i in liste:
        print(i)

#En funksjon som tar inn bokstav fra brukeren
def repetisjon():
    mineOrd = []
    inp = input("Skriv enten i, u eller s: ")
    while inp != "s":
#hvis brukeren skriver inn "i" ber programmet om to tekstrenger
#og legges inn i listen mineOrd
        if inp == "i":
            streng1 = input("Skriv her første streng: ")
            streng2 = input("Skriv her andre streng: ")
            mineOrd.append(slaaSammen(streng1,streng2))
            print (mineOrd)
            inp = input("Skriv enten i, u eller s: ")
#hvis brukeren skriver inn "u" kaller prosedyren skrivUt med mineOrd som parameter
        elif inp == "u":
            skrivUt(mineOrd)
            print (mineOrd)
            inp = input("Skriv enten i, u eller s: ")
#hvis brukeren skriver inn "s" går vi ut av løkken og avslutter programmet
        else: inp == "s"
#kjører funksjonen repetisjon
repetisjon()
