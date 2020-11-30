#Et program skriver ut det første og tredje elementet i listen, og legger deretter til et nytt tall på slutten av listen.
liste = [2, 4, 5]
liste.append(9)
print(liste[0], liste[2])
#Et program lager en ny liste som er tom og ber brukeren om å skrive inn 4 navn, og legger disse navn inn i listen.
navnlist = []
for i in range(4):
    navnlist.append(input("Skriv inn navn: "))
print(navnlist)
#Et program bruker en if-sjekk for å se om brukeren har lagt inn navnet sitt i lista
#hvis brukeren har gjort det skal programet skrive ut “Du husket meg!”.
#hvis navnet ikke finnes i listen da programmet skriver ut “Glemte du meg?”.
if 'Rokas' in navnlist :
    print("Du husket meg!")
else:
    print("Glemte du meg?")
#Et program lager en ny liste som slår sammen de to listene som var laget før, og skriver ut den nye listen.
nylist = liste + navnlist
print (nylist)
#Et program fjerner de to siste elementene fra listen, og skriver ut listen på nytt.
nylist.pop()
nylist.pop()
print (nylist)
