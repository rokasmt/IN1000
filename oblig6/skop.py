#På den første defineres funksjonen minFunksjon, som ikke tar imot noen parametere
#det samme med funksjonen hovedprogram og da kaller programmet på et hovedprogram
#i hovedprogramet oprettes "a" med 42, og "b" med 0
#etterpå skriver "b" ut, og på den måten "b" blir tildelt til "a" dvs 42

#Senere kalles minFunksjon, og starter en for loop med range 2
#Deretter blir "c" gitt verdien 2, og så skrev ut
#Etterpå blir "c" addet med én verdi høyere, og vil bli 3
#Deretter blir variablen b gitt verdien 10, og så addet på med verdien av en a
#Her finnes et problem. Variabelen a er ikke definer i minFunksjon
#og derfor programmet stopper

#Det er fordi funksjonen kan kun sjekke globale variabler og sine egne lokale variabler.
#"a"er kun definert i hovedprogramets funksjonen.


def​ minFunksjon​():
    for​ x ​in​ range​(​2​):
        c ​=​ 2
​        print​(​c)
        c ​+=​ 1
        b ​=​ ​10
        b ​+=​ a​
        print​(​b​)
    return​(​b​)
def hovedprogram():
    a ​=​ ​42
    b ​=​ 0
    print​(​b​)
    b ​=​ a
    a ​=​ minFunksjon​()
    print​ ​(​b​)
    print​ ​(​a​)

hovedprogram()
