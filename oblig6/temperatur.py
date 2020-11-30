#Bruker en fil temperatur.txt og leser inn temperaturene
#en etter en og putter verdiene inn i en liste
fil = open("temperatur.txt", "r")
liste = []
for linje in fil:
    liste.append(int(linje))
fil.close()
print(liste)
#Funksjonen som tar i mot en liste og returnerer gjennomsnittet
#av verdiene i listen ved hjelp av en før-lokke
def temperatur(liste):
    average = sum(liste) / len(liste)
    return average
print ("Gjennomsnittet av temperaturene er: ", temperatur(liste))
