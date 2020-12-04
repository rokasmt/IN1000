# Klasse for representasjon av racks i en regneklynge.
class Rack:
    # oppretter et rack der det senere kan plasseres noder
    def __init__(self):
        self._noder = []
# Plasserer en ny node inn i racket

    def settInn(self, node):
        self._noder.append(node)
# Henter antall noder i racket

    def getAntNoder(self):
        return len(self._noder)
# Beregner sammenlagt antall prosessorer i nodene i et rack

    def antProsessorer(self):
        antProsessorer = 0
        for node in self._noder:
            antProsessorer += node.antProsessorer()
        return antProsessorer
# Beregner antall noder i racket med minne over gitt grense

    def noderMedNokMinne(self, paakrevdMinne):
        antNoderMedNokMinne = 0
        for node in self._noder:
            if node.nokMinne(paakrevdMinne):
                antNoderMedNokMinne += 1
        return antNoderMedNokMinne
