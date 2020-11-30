from dato import Dato

def hovedprogram():
    #oppretter et objekt for en dato der dag er 15
    ny = Dato(15,9,1993)
    #skriver ut datoens år på terminalen
    print(ny.leserAar())
    #skriver ut "Loenningsdag!" på terminalen om datoen er en bestem dag i måneden
    ny.sjekkeDato(1)
    ny.sjekkeDato(15)
    #Lagrer datoen som en streng
    ny.lagStreng()
    #Skriver ut datoen på terminalen på en lesbar form

    #Endrer datoen til dagen etter og skriver den ut på nytt
    print(ny.endreDato(16,9,1993))

hovedprogram()
