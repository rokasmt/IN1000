#Funksjonen som har to parametre. Funksjonen returnerer summen av disse
#og skriver ut resultatet
def addisjon(parameter1, parameter2):
    sum = parameter1 + parameter2
    return (sum)

#Funksjonen som trekker det andre parameteret fra det første
def subtraksjon(parameter1, parameter2):
    return parameter1 - parameter2

#Funksjonen som deler det første parameteret fra det andre
def divisjon(parameter1, parameter2):
    return parameter1/parameter2

#Funksjonen som regner om fra tommer til centimeter
def tommerTilCm(antallTommer):
    antall = (antallTommer*2.54)
    return antall

#Funksjonen som inneholder forskjeligge funksjoner inni seg og skriver ut resultatene
def skrivBeregninger():
    print("Utregninger")
    a = int(input("Skriv inn tall 1: "))
    b = int(input("Skriv inn tall 2: "))
    print ("\n")
    print ("Resultat av summering: ", float(addisjon(a,b)))
    print ("Resultat av subtraksjon: ", float(subtraksjon(a,b)))
    print ("Resultat av divisjon: ", float(divisjon(a,b)))
    print ("\n")
    print ("Konvertering fra tommer til cm: ")
    c=float(input("Skriv inn et tall: "))
    tommerTilCm(c)
    print ("Resultat: ", tommerTilCm(c))

sum1 = addisjon(3,7)
#Skriver ut summene av tallene
print ("Summen av disse parametre er:", sum1)

#Tester funksjonene ved hjelp av assert
print(divisjon(-1,-1)) == 0, "Divisjonen feilet."
print(divisjon(-1,1)) == 0, "Divisjonen feilet."
print(divisjon(1,1)) == 0, "Divisjonen feilet."

#Tester funksjonene ved hjelp av assert
assert subtraksjon(1, 1) == 0, "Subtraksjonen riktig."
assert subtraksjon(-1, -1) == 0, "Subtraksjonen riktig."
assert subtraksjon(1, -1) == 2, "Subtraksjonen feilet."

print (tommerTilCm(20))
#Kjører funksjon skrivBeregninger
skrivBeregninger()
