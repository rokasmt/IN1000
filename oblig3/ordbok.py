#Et program lager en ordbok som inneholder varer in en butikk og pris.
def varene():
    varer = input("Skriv inn et varenavn: ")
    value = float(input("Skriv pris: "))
    varenavn[varer] = value
varenavn = {"Melk": 14.90, "Brød": 24.90, "Yoghurt": 12.90, "Pizza": 39.90}
print ("Varenavn:")
for key, value in varenavn.items() :
    print(key, value)
varene()
varene()
#Et program leser inn to varenavn og priser fra brukeren og legger disse til i ordboken.
print ("Varenavn:")
for key, value in varenavn.items() :
    print(key, value)
