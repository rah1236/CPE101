#function reads file line by line and prints
#str -> none
def readFile(file):
    f = open(file, "r")
    count = 0
    for line in f:
        print("Line " + str(count) + " (" + str(len(line)-1) + " chars): " + line)
        count+=1
readFile("in.txt")
