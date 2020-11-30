class Celle:
    # konstruktør
    def __init__(self):
        self._status = "død"

    # Endre status
    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

    # Hente status
    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hentStatusTegn(self):
        if self._status == "død":
            return(".")
        else:
            return("O")
