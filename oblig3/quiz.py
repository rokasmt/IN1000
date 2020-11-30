#En quiz spør brukeren om hovedstater i Skandinavia. Hvis brukeren svarer rett,
#gir programet svar fra ordboka, f.eks Hvis Norge, da svaret er Oslo;
#Hvis Sverige, da svaret er Stokholm, Hvis Denmark, da svaret er Kopenhagen,
#Hvis Finland, da svaret er Helsinki, Hvis Island, da svaret er Rejkavik.
#men hvis brukeren skriver feil, skriver programet "Dette landet finnes ikke i databasen"
Hovedstater = {"Norge": "Oslo",
"Sverige": "Stokholm",
"Denmark": "Kopenhagen",
"Finland": "Helsinki",
"Island": "Rejkavik"}

sporsmal = input("Hvilket land vil du vite hovedstaten i?").capitalize()

if sporsmal in Hovedstater:
    print("Hovedstaten i " + sporsmal + " er " + Hovedstater[sporsmal])
else:
    ("Dette landet finnes ikke i databasen")
