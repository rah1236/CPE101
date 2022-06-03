from imageFuncs import *

fileName = input("Hi, which image would you like to modify?, if it's not in this folder, include the path: ")

image = Image(fileName)

modification = input("Which modificaion would you like to make? [negate, high_contrast, grayscale, remove_color]: ")
while(modification != "negate" and modification != "high_contrast" and modification != "grayscale" and modification != "remove_color"):
    print("That's not one of the available options, try again.")
    modification = input("Which modificaion would you like to make? [negate, high_contrast, grayscale, remove_color]:")
colorRemoved = ""
if modification == "remove_color":
    RGB = ["R", "G", "B"]
    colorRemoved = (input("What color do you want removed? [R, G, B]: ")).upper()
    while(colorRemoved != "R" and colorRemoved != "G" and colorRemoved != "B"):
        print("That isn't one of the available options, try again.")
        colorRemoved = (input("What color do you want removed? [R, G, B]: ")).upper()
    image.process_body(modification, RGB.index(colorRemoved))
else:
    image.process_body(modification)
