from spillebrett import Spillebrett


def main():
    spill = Spillebrett(25, 25)
    spill.tegnBrett()

    brukerInput = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:")

    while brukerInput != "q":
        spill.oppdatering()
        spill.tegnBrett()

        brukerInput = input(
            "Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:")


# starte hovedprogrammet
main()
