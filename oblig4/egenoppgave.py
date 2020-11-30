#Programmet tar informasjonen om elevenes karakterer fra liste
#og bruker for-løkker til å finne hvilke gjennomsmitt(god eller dårlig) har elevene, og skriver ut dette.
Karakter = [
  ['Christer', 10, 6, 8],
  ['Dora', 2, 2, 2, 3, 3, 10, 10, 10, 10, 9, 1, 10],
  ['Emma', 10, 10, 4],
  ['Peter', 10, 10],
  ['Peter', 10, 10, 1, 1, 1, 10, 10, 10, 10, 10, 9],
  ['Jonas', 10, 10, 7, 10, 1],
  ['Olav', 5, 5, 5, 4, 8, 8, 2],
  ['Kristine', 8, 10, 0, 10, 9, 9, 7]
]
#før-løkken sjekker om elevenenes gjennomsmitt er god eller dårlig
for string in Karakter:
  navnet = string[0]
  nummer = string[1:] # vi tar ikke element som er 0(er) i liste.
  gjennomsmitt = sum(nummer) / len(nummer)
  if gjennomsmitt > 4 and min(nummer) > 2:
    resultat = 'GOD'
  else:
    resultat = 'DAARLIG'
  print(navnet, gjennomsmitt, resultat)
