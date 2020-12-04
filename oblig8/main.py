from Node import Node
from regneklynge import Regneklynge


def hovedprogram():

    abel = Regneklynge(12)
    node1 = Node(64, 1)
    node2 = Node(1024, 2)

    node1telle = 650
    while node1telle > 0:
        abel.settInnNode(node1)
        node1telle -= 1

    node2telle = 16
    while node2telle > 0:
        abel.settInnNode(node2)
        node2telle -= 1

    minne32 = abel.noderMedNokMinne(32)
    minne64 = abel.noderMedNokMinne(64)
    minne128 = abel.noderMedNokMinne(128)
    antallProsessorer = abel.antProsessorer()
    antallRacks = abel.antRacks()

    print("Antall med minst 32 GB: ", minne32)
    print("Antall med minst 64 GB: ", minne64)
    print("Antall med minst 128 GB: ", minne128)

    print("Antall prosessorer: ", antallProsessorer)

    print("Antall rack: ", antallRacks)


hovedprogram()
