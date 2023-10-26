from typing import Dict


def inlezen_morse_bestand(bestandsnaam:str) ->Dict[str,str]:
    dict_morse = {}
    fo = open(bestandsnaam)
    fo.readline()
    lijnen = fo.read().splitlines()
    #opm: de eerst slaan we over door te starten op positie 1 ( en niet 0)
    for lijn in lijnen[1:]:
        delen = lijn.split(";")
        letter = delen[0]
        morse_teken = delen[1]
        dict_morse[letter] = morse_teken    # <--- toevoegen aan dict. letter is de key, morse is value


    fo.close()
    return dict_morse




def vertaal_letter(letter: str, dict_morse:Dict[str,str]) -> str:
    #zet eventueel de letter om naar kleine letter
    letter = letter.lower()
    if letter in dict_morse.keys():
        morse = dict_morse[letter]
        return morse
    else:
        return "?"

def vertaal_tekst_in_morse(zin:str, dict_morse:Dict[str,str]) -> str:
    result = ""
    for letter in zin:
        #vertaal de letter naar morse
        morse = vertaal_letter(letter, dict_morse)
        #voeg toe aan resultaat
        result = result + " " + morse


    return result









dict_morse = inlezen_morse_bestand("doc/morse.txt")
print(dict_morse)
letter = input("Geef een letter op:> ")
morse_teken = vertaal_letter(letter, dict_morse)
print(f"Het morse teken is: {morse_teken}")

zin = input("Geef een zin op:> ")
morse_vertaling = vertaal_tekst_in_morse(zin, dict_morse)
print(f"De vertaling van de zin is {morse_vertaling}")