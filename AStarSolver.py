import PIL.Image as Image
import math

class Node:
    def __init__(self, coordinate, h):
        self.coord = coordinate
        self.parent = None
        self.Hvalue = h
        self.fvalue = math.inf


def getEnds(image):
    width, height = image.size

    topRow = 0
    botRow = height - 1

    topCoord = None
    botCoord = None

    for col in range(0, width):
        tCoord = (col, topRow)
        bCoord = (col, botRow)
        if image.getpixel(tCoord) == (255, 255, 255):
            topCoord = tCoord
        if image.getpixel(bCoord) == (255, 255, 255):
            botCoord = bCoord

    return (topCoord, botCoord)

def load_image(file_path):
    image = Image.open(file_path)
    image = image.convert('RGB')
    return image

def create_graph(image, end):
    endX = end[0]
    endY = end[1]

    graph = {}

    width, height = image.size
    for row in range(0, height):
        for col in range(0, width):

            coord = (col, row)

            if(image.getpixel(coord) == (255, 255, 255)):

                hX = int(math.fabs(col - endX))
                hY = int(math.fabs(row - endY))

                node = Node(coord, hX + hY)
                graph[coord] = node

    return graph

def AStar(graph, current, end, open, closed):
    north = (current[0], current[1] - 1)
    south = (current[0], current[1] + 1)
    east = (current[0] + 1, current[1])
    west = (current[0] - 1, current[1])



def get_nodes(file_path):

    #load the image
    image = load_image(file_path)

    #Get the start and end points
    start, end = getEnds(image)

    #Create the graph
    graph = create_graph(image, end)

    #Empty open and closed list
    open = []
    closed = []

    #Use the AStar
    AStar(graph, start, end, open, closed)
