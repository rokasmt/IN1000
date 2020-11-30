list = []
tall = int(input("Tast et heltall: "))
#en while-løkke leser inn tall fra brukeren helt til brukeren taster 0
while tall != 0:
    list.append(tall)
    tall = int(input("Tast et heltall: "))
#Går gjennom lista og skriver ut hvert enkelt element.
for element in list:
    print (element)
#Skriver ut summen til brukeren
minSum = 0
for x in list:
      minSum = minSum + x
print("Summer er: ", minSum)
#Skriver ut det minste elementet i lista
minste = list[0]
for x in list:
    if x < minste:
        minste = x
print ("Minste tall i liste er:", minste)
#Skriver ut det største elementet i lista
største = list[0]
for y in list:
    if y > største:
        største = y
print ("Største tall i liste er:", største)
