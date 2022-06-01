class Image:
    #inits image class
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
            content.append(line)
        self.content = content
#decodes hidden image into result ppm
#none -> none
    def decoder(self):
        imageList = []
        currentPixel = []
        count = 0
        print(self.content[3])
        for color in range(3, (self.height * self.width * 3) + 3):
            currentPixel.append(int(image.content[color]))
            count += 1
            if count == 3:
                count = 0
                imageList.append(currentPixel)
                currentPixel = []
        print(len(imageList) * 3)

        for pixel in imageList:
            if pixel[0] * 10 > self.colorDepth:
                pixel[0] = self.colorDepth
            else:
                pixel[0] = pixel[0] * 10
            pixel[1] = pixel[0]
            pixel[2] = pixel[0]
        newFile = open("result.ppm", "w")
        newFile.write("P3\n")
        newFile.write(str(self.width) + " " + str(self.height) + "\n")
        newFile.write(str(self.colorDepth) + "\n")
        for pixel in imageList:
            for color in pixel:
                newFile.write(str(color) + "\n")




image = Image("hidden.ppm")

image.decoder()
