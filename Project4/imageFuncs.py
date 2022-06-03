R = 0 #constants to make managing pixel colors a little more readable
G = 1
B = 2

#image class allows ppm to be managed as an object instead of a list.
class Image:
    #inits image class
    #str - > none
    def __init__(self, name):
        f = open(name, "r")

        f.readline()
        widthAndHeight = f.readline().split()
        width = int(widthAndHeight[0])
        height = int(widthAndHeight[1])
        colorDepth = int(f.readline())
        self.name = name
        self.width = width
        self.height = height
        self.colorDepth = colorDepth
        f.close()
        f = open(name, "r")
        content = []
        for line in f:
            lineSplit = line.split()
            for chunk in lineSplit:
                content.append(chunk)
        self.content = content
        imageDataList = []
        currentPixel = []
        count = 0
        #print(self.content[3])
        for color in range(4, (self.height * self.width * 3) + 4):
            currentPixel.append(int(self.content[color]))
            count += 1
            if count == 3:
                count = 0
                imageDataList.append(currentPixel)
                currentPixel = []
        self.content = imageDataList

# writes new ppm files
#list str -> none
    def write_file(self, list, modification):
        newFile = open(self.name[:-4] + "_" + modification +"_result.ppm", "w")
        newFile.write("P3\n")
        newFile.write(str(self.width) + " " + str(self.height) + "\n")
        newFile.write(str(self.colorDepth) + "\n")
        for pixel in list:
            for color in pixel:
                newFile.write(str(color) + "\n")

#processes ppm files depending on modification input
#str, int - > none
    def process_body(self, modification, color:int = 0):
            newImageDataList = []
            if modification == "negate":
                for pixel in self.content:
                    pixel[R] = 255 - pixel[R]
                    pixel[B] = 255 - pixel[B]
                    pixel[G] = 255 - pixel[G]
                    newImageDataList.append(pixel)
            elif modification == "high_contrast":
                for pixel in self.content:
                    for RGB in range(0,3):
                        if pixel[RGB] > 127:
                            pixel[RGB] = 255
                        else:
                            pixel[RGB] = 0
                    newImageDataList.append(pixel)
            elif modification == "grayscale":
                for pixel in self.content:
                    averageColor = int(sum(pixel)/3)
                    for RGB in range(0,3):
                        pixel[RGB] = averageColor
                    newImageDataList.append(pixel)
            elif modification == "remove_color":
                for pixel in self.content:
                    pixel[color] = 0
                    newImageDataList.append(pixel)

            self.write_file(newImageDataList, modification)
            print("done!")
