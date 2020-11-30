#Et program som ber bruker om aa svare paa spoærsmaalet "Hva er etternavnet til Erna?", hvis man har svart riktig skal programmet skrive ut "Du har rett".
#Hvis ikke skal programmet skrive ut "Desverre, svaret var" og deretter det riktige svaret som er "Solberg"
svar = input("Hva er etternavnet til Erna?" '\n')
rett = "Solberg"
if svar.upper() == rett.upper() :
    print("Du har rett!")
else :
    print("Desverre, svaret var", rett)
