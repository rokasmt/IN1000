#Oppgaveteksten:
#Skriv et beregningsprogram for skreddere med en funksjon
#som leser inn en fil der hver linje beskriver et navn
#på et mål og selve målet i tommer

#La programmet legge disse målene i en ordbok
#med navn på målet som nøkkelverdi og returner ordboken

#Lag deretter en prosedyre som tar imot en liste
#av mål og benytter seg av ​tommerTilCm​  for å skrive ut målene i centimeter

#En prosedyre som tar imot en liste av mål og benytter seg av ​tommerTilCm​
def tommerTilCm(antallTommer):
    assert antallTommer>=0
    antall=(antallTommer*2.54)
    return antall
#Funksjonen  som leser inn en fil der hver linje beskriver
#et navn på et mål og selve målet i tommer.
fil = open("egenoppgave.txt", "r")
ordbok = {}

for linje in fil:
    biter = linje.split()
    ordbok[biter[0]] = float(biter[1])

fil.close()
print(ordbok)
#en prosedyre som tar imot en liste av mål og benytter seg av
#tommerTilCm for å skrive ut målene i centimeter
for maal, tommer in ordbok.items():
    print(maal, tommerTilCm(tommer))
