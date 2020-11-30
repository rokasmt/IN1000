#En funksjon tar to heltall som parametere
def adder (tall1, tall2):
    sum = tall1+tall2
    return (sum)
sum1 = adder(2,5)
sum2 = adder(4,6)
#Skriver ut summene av tallene
print ("Første sum er:", sum1)
print ("Den andre sum er:", sum2)
#En funksjon teller hvor mange ganger en bokstav ​minBokstav​ forekommer
#i teksten ​"minTekst​" og returnere dette tallet
def tellForekomst(minTekst, minBokstav):
    while len(minBokstav)>1:
        minBokstav =("Skriv en tekstreng:")
    return(minTekst.count(minBokstav))
tekst = input("Kan du skrive en setning?")
bokstav = input("Kan du skrive en bokstav?")

antall = tellForekomst(tekst,bokstav)

print("En bokstav", bokstav, "forekommer", antall, "ganger i teksten")
