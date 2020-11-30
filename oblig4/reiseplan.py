#Lager en tom liste ​steder, og gir brukeren mulighet til å fylle den
#med 5 reisemål ved hjelp av en før-løkke
steder = []
for i in range (5):
    x =input("Skriv sted: ")
    steder.append(x)
print (steder)
#Lager en list og la brukeren fylle inn med fem elementer i liste
klesplagg = []
for i in range (5):
    y =input("Skriv klesplagg: ")
    klesplagg.append(y)
print (klesplagg)
#Lager en list og la brukeren fylle inn med fem elementer i liste
avreisedatoer = []
for i in range (5):
    z =input("Skriv avreisedatoer: ")
    avreisedatoer.append(z)
print (avreisedatoer)
#Lage en liste som inneholder de andre listene jeg har skrevet
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)
print (reiseplan)
#Bruk en enkel for-løkke for å skrive ut innholdet i ​reiseplan​,
#og ser at det skrives ut tre lister med hvert sitt innhold.
for element in reiseplan:
    print(element)
#Brukeren oppgir en plass i ​reiseplan​ og skriver ut elementet på den oppgitte plassen
i1 = int(input("Vil du hente steder(0), klesplagg(1) eller avreisedatoer(2)? "))
i2 = int(input("Velg et av de fem elementene: "))
#Bruker en if-sjekk til å teste at de to tallene brukeren har oppgitt er gyldige verdier
#Hvis tallene er mulige plasser i listene skal de brukes til å skrive ut reiseplan ​[i1][i2]​
#Hvis tallene ikke er gyldige plasseringer skal skrive ut “Ugyldig input!”
if (0 <= i1 < 3 and 0 <= i2 < 5):
    print (reiseplan[i1][i2])
else:
    print("Ugyldig input!")
