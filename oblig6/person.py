class Person:

    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def leggTilHobby(self, hobby):
        self._hobbyer.append(hobby)

    def skrivHobbyer(self):
        hobbyer = ""
        for i in self._hobbyer:
            hobbyer += i + ","
        print (hobbyer)

    def skrivUt(self):
        print("Navn:", self._navn, "Alder:", self._alder)
        Person.skrivHobbyer(self)
