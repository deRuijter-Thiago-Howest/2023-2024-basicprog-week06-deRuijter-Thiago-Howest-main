# Maak de functie ‘vul_bestand_aan’. Deze functie is analoog aan de vorige functie
# ‘schrijf_input_naar_bestand’ behalve dat het bestand onderaan verder aangevuld wordt (en de
# bestaande inhoud dus niet gewist wordt). Test uit.

import os

def lees_bestand_in(bestandsnaam: str) -> None:
    fo = open(bestandsnaam) #file object
    inhoud = fo.read().splitlines()  # <---- splitlines geeft een list van de lijnen uit het bestand terug
        
    regelnummer = 1
        
    for lijn in inhoud:
        print(f"Regel {regelnummer}: {lijn}")
        regelnummer += 1


    fo.close()



def schrijf_input_naar_bestand(bestandsnaam:str) -> None:
    fo = open(bestandsnaam, "w")   # vergeet niet de rechten goed te zetten (via de letter "w")

    lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")
    while lijn != "":
        fo.write(lijn + "\n")  # <-----!!! pas op; vergeet het newline karakter niet!
        lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")

    fo.close()



def vul_bestand_aan(bestandsnaam:str) -> None:
    fo = open(bestandsnaam, "a")   # "a" het bestand wordt aangevuld.

    lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")
    while lijn != "":
        fo.write(lijn + "\n")  # <-----!!! pas op; vergeet het newline karakter niet!
        lijn = input("Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test:> ")

    fo.close()

#de inhoud van een bestand wordt continu overgeschreven
# schrijf_input_naar_bestand("doc/temp.txt")
# lees_bestand_in("doc/temp.txt")

vul_bestand_aan("doc/temp.txt")
lees_bestand_in("doc/temp.txt")