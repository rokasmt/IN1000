from motorsykkel import Motorsykkel

def hovedprogram():

    en = Motorsykkel("TESLA", "999", 5000)
    to = Motorsykkel("BMW", "111", 100)

    en.skrivUt()
    to.skrivUt()

    to.kjor(10)
    print(to.hentKilometerstand())

hovedprogram()
