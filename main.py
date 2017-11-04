import PIL.Image as Image

import BasicNodeTrasposer

image = Image.open("small.bmp")
image = image.convert('RGB')

width, height = image.size;

#for col in range(0, width):
#    print(str(col) + " " + str(image.getpixel((col, 0))))

BasicNodeTrasposer.get_graph(image)
