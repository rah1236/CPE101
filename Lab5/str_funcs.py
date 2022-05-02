
# Name: Raheel Rehmatullah
# Section: 7

#purpose: Input a string and make it all caps
#str -> str
def whole_str_capitalize(string):
    newString = ""
    for char in string:
        if ord(char) > 90:
            char = chr(ord(char) - 32)
        newString += char
    return(newString)

#purpose: Take a string and make the first char caps
#str->str
def str_capitalize(string):
    newString = ""
    for char in string:
        if len(newString) == 0:
            newString += whole_str_capitalize(char)
        else:
            newString += char
    return(newString)


#Purpose: Input a string and return the vowels in the string in the order they appear
#str -> str
def vowel_extractor(string):
    vowels = ""
    for i in string:
        char = i
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U" or char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels += char
    return (vowels)

#Purpose: Cypther the letters in a string by 13 via the ROT13 standard
#str -> str
def str_rotate(string):
    newString = ""
    for character in string:
        char = ord(character)
        if (char < 90) and ( char > 78):
            newString += chr(char - 13)
        elif(char < 122 and char > 110):
            newString += chr(char - 13)
        elif(char < 78 and char > 65):
            newString += chr(char + 13)
        elif (char < 109) and (char > 97):
            newString += chr(char + 13)
        else:
            newString += character
    return(newString)

#purpose :This function returns a substring that begins from start index and ends at stop index and increasing step characters.
#str int int int -> str
def make_substring(string, start, stop, index):
    newString = ""
    for i in range(start, stop, index):
        newString += string[i]
    return(newString)

#This  function  takes  a  string  as  input  and  returns  True  if  string  is  palindrome  and  False otherwise.
#str -> bool
def is_palindrome(string):
    stringRev = ""
    for i in range(len(string)-1, -1, -1):
        stringRev += string[i]
    if string != stringRev:
        return False
    else:
        return True

#purpose count the number of a certain char in a string
#str str -> int
def count_characters(string, char):
    count = 0
    for character in string:
        if character == char:
            count += 1
    return(count)
