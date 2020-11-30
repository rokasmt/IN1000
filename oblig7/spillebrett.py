from random import randint
from celle import Celle


class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0
        self._todimensjonalListe = []

        for i in range(self._rader):
            indreListe = []

            for j in range(self._kolonner):
                indreListe.append(Celle())

            self._todimensjonalListe.append(indreListe)

        self.generer()

    def tegnBrett(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self._todimensjonalListe[i][j].hentStatusTegn(), end=" ")
            print()

        print("Generasjon:", self._generasjonsnummer)
        print("Antall levende celler:", self.finnAntallLevende())

    def oppdatering(self):
        doed_liste = []
        levende_liste = []

        for i in range(self._rader):
            for j in range(self._kolonner):
                levendeNaboer = 0

                naboer = self.finnNabo(j, i)

                for nabo in naboer:
                    if nabo.erLevende():
                        levendeNaboer += 1

                if self._todimensjonalListe[i][j].erLevende():
                    if levendeNaboer < 2 or levendeNaboer > 3:
                        doed_liste.append(self._todimensjonalListe[i][j])
                else:
                    if levendeNaboer == 3:
                        levende_liste.append(self._todimensjonalListe[i][j])

        for celle in doed_liste:
            celle.settDoed()
        for celle in levende_liste:
            celle.settLevende()

        self._generasjonsnummer += 1

    def finnAntallLevende(self):
        levendeCeller = 0

        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._todimensjonalListe[i][j].erLevende():
                    levendeCeller += 1

        return levendeCeller

    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                if randint(0, 2) == 0:
                    self._todimensjonalListe[i][j].settLevende()

    def finnNabo(self, x, y):
        naboer = []

        for i in range(y - 1, y + 2):
            if 0 < i < self._rader:
                for j in range(x - 1, x + 2):
                    if 0 < j < self._kolonner:
                        if x != j or y != i:
                            naboer.append(self._todimensjonalListe[i][j])
        return naboer
