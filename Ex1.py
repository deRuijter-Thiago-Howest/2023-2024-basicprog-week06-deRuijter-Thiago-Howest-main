#oefening 1

def lees_bestand_in(bestandsnaam: str) -> None:
    fo = open(bestandsnaam) #file object
    inhoud = fo.read().splitlines()  # <---- splitlines geeft een list van de lijnen uit het bestand terug
    
    regelnummer = 1
    
    for lijn in inhoud:
        print(f"Regel {regelnummer}: {lijn}")
        regelnummer += 1


    fo.close()

lees_bestand_in("doc/MyFile.txt")