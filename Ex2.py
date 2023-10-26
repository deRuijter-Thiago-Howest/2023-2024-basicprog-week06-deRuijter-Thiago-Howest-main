# Maak een applicatie die controleert of een bestand ‘temp.txt’ wel of niet bestaat.
# Wanneer het bestand bestaat, dan wordt de functie ‘lees_bestand_in’ uit de vorige oefening
# aangeroepen.
# Wanneer het bestand nog niet bestaat, wordt de functie ‘schrijf_input_naar_bestand’ aangeroepen.
# Deze functie maakt een nieuw bestand aan (met de bestandsnaam als parameter). Vervolgens vragen
# we meermaals aan de gebruiker om een lijn op te geven. Elke nieuwe lijn wordt onmiddellijk naar het
# bestand weggeschreven.
import os

def lees_bestand_in(bestandsnaam: str) -> None:
    fo = open(bestandsnaam) #file object
    inhoud = fo.read().splitlines()  # <---- splitlines geeft een list van de lijnen uit het bestand terug
        
    regelnummer = 1
        
    for lijn in inhoud:
        print(f"Regel {regelnummer}: {lijn}")
        regelnummer += 1


    fo.close()

    lees_bestand_in("doc/temp.txt")


def schrijf_input_naar_bestand(bestandsnaam:str) -> None:
    fo = open(bestandsnaam, "w")   # vergeet niet de rechten goed te zetten (via de letter "w")

    lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")
    while lijn != "":
        fo.write(lijn + "\n")  # <-----!!! pas op; vergeet het newline karakter niet!
        lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")

    fo.close()

if os.path.exists("doc/temp.txt"):
    lees_bestand_in("doc/temp.txt")
else:
    schrijf_input_naar_bestand("doc/temp.txt")