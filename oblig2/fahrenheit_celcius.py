#Brukeren skriver ut temperaturen i fahrenheit og programme regner temperaturen fra fahrenheit til celcius.
fahrenheit= float(input("Skriv temperatur i fahrenheit: "))
fahrenheit = int(fahrenheit)
celcius = float(((fahrenheit)- 32) * 5/9)
print("%.2f" % celcius)
