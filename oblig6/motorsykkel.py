class Motorsykkel:

    def __init__(self, merke, regNr, kilometerstand):
        self._merke = merke
        self._registreringsnummer = regNr
        self._kilometerstand = kilometerstand

    def kjor(self, km):
        self._kilometerstand += km

    def hentKilometerstand(self):
        return self._kilometerstand


    def skrivUt(self):
        print("Merke:", self._merke)
        print("Reg.Nr:", self._registreringsnummer)
        print("Kilometerstand:", self._kilometerstand)
        print()
