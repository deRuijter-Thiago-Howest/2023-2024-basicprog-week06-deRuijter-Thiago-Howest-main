import random
from typing import List

def inlezen_spelers(bestandsnaam:str) -> List[str]:
    list_spelers = []
    fo = open(bestandsnaam, "r")
    inhoud = fo.read().splitlines()
     
    for lijn in inhoud:
        list_spelers.append(lijn)
        
    return list_spelers

def print_spelers(list_spelers: List[str], ploegnaam:str) ->None :
    print(f"Naam: {ploegnaam}")
    nummer_speler = 1 
    for speler in list_spelers:
        print(f"{nummer_speler}:{speler}")
        nummer_speler += 1

def selecteer_random_elftal(list_spelers:List[str])-> List[str]:
    elftal = []
    while len(elftal) < 11:
        speler = random.choice(list_spelers)
        if speler not in elftal:
            elftal.append(speler)
    return elftal
    # elftal = []
    # while len(elftal) != 11:
    #     speler = random.choice(list_spelers)
    #     if speler not in elftal:
    #         elftal.append(speler)
    # return elftal

def opslaan_ploegopstelling(bestandsnaam:str, elftal: List[str], ploegnaam:str)-> None:
    fo = open(bestandsnaam,"w")
    fo.write(f"Ploegnaam: {ploegnaam} \n")
    nummer = 1
    for speler in elftal:
        fo.write(f"{nummer} : {speler}\n")
        nummer += 1
    fo.close()


mct_spelers = inlezen_spelers("doc/Players.txt")
# print_spelers(mct_spelers,"ploeg MCT rules")

mijn_elftal = selecteer_random_elftal(mct_spelers)
print_spelers(mijn_elftal, "Mijn elftal uit MCT")
opslaan_ploegopstelling("doc/opstelling.txt", mijn_elftal, "Mijn elftal uit MCT" )