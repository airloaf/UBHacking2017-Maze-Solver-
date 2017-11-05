import PIL.Image as Image
import math

class Node:
    def __init__(self, coordinate, h):
        self.coord = coordinate
        self.parent = None
        self.hValue = h
        self.fValue = math.inf


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

    if current == end:
        return

    closed.append(current)

    north = (current[0], current[1] - 1)
    south = (current[0], current[1] + 1)
    east = (current[0] + 1, current[1])
    west = (current[0] - 1, current[1])

    AStar_check_neighbor(graph, current, north, open, closed)
    AStar_check_neighbor(graph, current, south, open, closed)
    AStar_check_neighbor(graph, current, east, open, closed)
    AStar_check_neighbor(graph, current, west, open, closed)

    if len(open) < 1:
        return

    smallest = None
    lowestF = math.inf

    for i in open:
        if graph[i].fValue < lowestF:
            lowestF = graph[i].fValue;
            smallest = i;

    AStar(graph, smallest, end, open, closed)

def AStar_check_neighbor(graph, current, neighbor, open, closed):
    #Check if the neighbor is in the graph
    if neighbor not in graph:
        return
    if neighbor in closed:
        return

    gVal = 10

    newF = gVal + graph[neighbor].hValue

    #Check if the f values are less than the old ones
    if(newF < graph[neighbor].fValue):
        graph[neighbor].parent = current
        graph[neighbor].fValue = newF

    if neighbor not in open:
        open.append(neighbor)

def get_nodes(image):

    #Get the start and end points
    start, end = getEnds(image)

    #Create the graph
    graph = create_graph(image, end)

    #Empty open and closed list
    open = []
    closed = []

    #Use the AStar
    AStar(graph, start, end, open, closed)

    queue = []

    #par = graph[end].parent

    par = end;
    while par != None:
        queue.append(par)
        par = graph[par].parent

    print(par)

    return queue

