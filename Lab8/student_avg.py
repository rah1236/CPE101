f = open("std_info.txt", "r")
gradeList = []
for line in f:
    gradeList.append(line.split())
for grade in gradeList:
    grade.pop(0)
    grade.pop(0)
EEgrades = []
CPEgrades = []
BUSgrades = []
ARTgrades = []
totalGrade = []
for grade in gradeList:
    if grade[0] == "EE":
        EEgrades.append(float(grade[1]))
    if grade[0] == "CPE":
        CPEgrades.append(float(grade[1]))
    if grade[0] == "BUS":
        BUSgrades.append(float(grade[1]))
    if grade[0] == "ART":
        ARTgrades.append(float(grade[1]))
    totalGrade.append(float(grade[1]))
print("EE average = " + str(sum(EEgrades)/len(EEgrades)))
print("CPE average: " + str(sum(CPEgrades)/len(CPEgrades)))
print("BUS average: " + str(sum(BUSgrades)/len(BUSgrades)))
print("ART average: " + str(sum(ARTgrades)/len(ARTgrades)))
print("Total average = " + str(sum(totalGrade)/len(totalGrade)))
