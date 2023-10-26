from typing import Dict
from typing import List




def inlezen_score_student(bestandsnaam:str) ->Dict[str,List] :
    dict_studenten = {}
    fo = open(bestandsnaam)
    lijnen = fo.read().splitlines()
    for lijn in lijnen:
        delen = lijn.split(":")      # <---- string opsplitsen op basis van : 
        naam = delen[0]
        score1 = int(delen[1])
        score2 = int(delen[2])
        score3 = int(delen[3])
        score4 = int(delen[4])
        score5 = int(delen[5])
        #toevoegen aan dict
        dict_studenten[naam] = [score1,score2,score3,score4,score5]

    fo.close()
    return dict_studenten

def zoek_en_print_student(naam:str, dict_studenten:Dict[str,List[int]]):
    #opzoeken in de dictionary
    #versie 1: exacte naam nodig anders wordt er niets teruggegeven.
    # if naam in dict_studenten.keys():
    #     scores = dict_studenten[naam]
    #     print(f"Gevonden student: {naam}")
    #     print(f"De scores van de student zijn: {scores}")

    #versie 2: een deel van de naam werd ingetikt. en nu?
    for student in dict_studenten.keys():
        #komt het deel voor in de student?
        if naam.lower() in student.lower():
            #bingo
            scores = dict_studenten[student]
            print(f"Gevonden student: {student}")
            print(f"De scores van de student zijn: {scores}")
            #gem berekenen en afprinten
            gemiddelde = sum(scores) / 5
            print(f"De gemiddelde score is: {gemiddelde:.2f}/20")


    


dict_studenten = inlezen_score_student("doc/scores.txt")
print(dict_studenten)
naam_student = input("Geef de naam van een student op:")
zoek_en_print_student(naam_student, dict_studenten)