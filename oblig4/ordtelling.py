#En funksjon som returnerer antall bokstaver i det angitte ordet.
def ord(a):
    return len(a)
#En funksjon som  returnerer ei ordbok hvor hvert ord i setningen er en nøkkelverd
#med antall ganger det ordet finnes i setningen, som innholdsverdi.
def ordbok(setning):
    mineList = setning.lower().split()
    mineOrdb = {}

    for word in mineList:
        if word not in mineOrdb:
            mineOrdb[word] = mineList.count(word)

    return mineOrdb
#Et program tar en setning fra brukeren og bruker begge funksjonene "ord" og "ordbok"
# og skriver ut til brukeren hvor mange ord det er i setningen
# og etterpå bruker resultatene fra de to funksjonene til å skrive
#hvor mange ganger hvert unike ord forekommer
#og hvor mange bokstaver hvert ord består av
setning= input("Skriv en setning:")
print (setning)
print ("Det er", len(setning.split()), "ord i setningen din.")
ord_i_setning = ordbok(setning)
for word, antall in ord_i_setning.items():
    if (word) ==1 and (antall) ==1:
        print("Ordet", word, "forekommer", antall, "ganger, og har", ord(word), "bokstaver")
    elif ord(word) >1 and (antall) == 1:
        print("Ordet", word, "forekommer", antall, "gang, og har", ord(word), "bokstav")
    elif (word) == 0 and (antall) > 0:
        print("Ordet", word, "forekommer", antall, "gang, og har", ord(word), "bokstav")
    else:
        print("Ordet", word, "forekommer", antall, "gang, og har", ord(word), "bokstav")
