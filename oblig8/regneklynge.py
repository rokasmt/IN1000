from rack import Rack

# Klasse for representasjon av regneklynge med racks og noder


class Regneklynge:
    # Oppretter tom regneklynge (for racks med oppgitt maxtall noder/ rack)
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._rackListe = []

# Plasserer en node inn i et rack med ledig plass, eller i et nytt
    def settInnNode(self, node):
        if len(self._rackListe) == 0 or self._rackListe[-1].getAntNoder() == self._noderPerRack:
            self._rackListe.append(Rack())
        self._rackListe[-1].settInn(node)

# Beregner totalt antall prosessorer i hele regneklyngen
    def antProsessorer(self):
        antProsessorer = 0
        for rack in self._rackListe:
            antProsessorer += rack.antProsessorer()
        return antProsessorer

# Beregner antall noder i regneklyngen med minne over angitt grense
    def noderMedNokMinne(self, paakrevdMinne):
        antNoderMedNokMinne = 0
        for rack in self._rackListe:
            antNoderMedNokMinne += rack.noderMedNokMinne(paakrevdMinne)
        return antNoderMedNokMinne

# Henter antall racks i regneklyngen
    def antRacks(self):
        return len(self._rackListe)
