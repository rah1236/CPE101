f = open("std_info.txt", "r")
newFile = open("student_avg.txt", "w")

gradeList = []
for line in f:
    gradeList.append(line.split())
    newFile.write(line)

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

newFile.write("\n")
newFile.write("EE average: " + str(sum(EEgrades)/len(EEgrades)) + "\n")
newFile.write("CPE average: " + str(sum(CPEgrades)/len(CPEgrades)) + "\n")
newFile.write("BUS average: " + str(sum(BUSgrades)/len(BUSgrades))+ "\n")
newFile.write("ART average: " + str(sum(ARTgrades)/len(ARTgrades))+ "\n")
newFile.write("Total average = " + str(sum(totalGrade)/len(totalGrade))+ "\n")
