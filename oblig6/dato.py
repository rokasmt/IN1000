class Dato:

    def __init__(self,nyDag,nyMaaned,nyAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyAar = nyAar

    def leserAar(self):
        return self._nyAar

    def lagStreng(self):
        print("Dagen", self._nyDag, "Måned", self._nyMaaned, "Året",self._nyAar)

    def sjekkeDato(self, dag):
        if dag == 15:
            print("Loenningsdag!")
        elif dag == 1:
            print("Ny maaned, nye muligheter!")

    #En metode som endrer datoen til neste dag
    def endreDato(self, nyDag, nyMaaned, nyAar):
        nyDato = nyDag, nyMaaned, nyAar
        return nyDato
