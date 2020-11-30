from hund import Hund

def hovedprogram():

    en = Hund(1, 7)
    to = Hund(11, 15)

    en.spring()
    en.spis(7)
    print(en.hentVekt())

    to.spring()
    to.spis(3)
    print(to.hentVekt())

hovedprogram()
