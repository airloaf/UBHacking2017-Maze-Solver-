'''
Assumes image is of type PIL.Image
and that image is of RGB pixels
'''
def get_graph(image):
    graph = transpose_nodes(image)

    get_neighbors(graph)

    width, height = image.size

    print_graph(graph, width, height )

    return graph

def print_graph(graph, width, height):
    for row in range(0, height):
        for col in range(0, width):
            coord = (col, row)

            if coord in graph:
                print(str(coord) + " - " + str(graph[coord]))


def get_neighbors(graph):
    for coord in graph:
        #Check the north south west and east neighbors
        north = (coord[0]-1, coord[1])
        south = (coord[0]+1, coord[1])
        west = (coord[0], coord[1] - 1)
        east = (coord[0], coord[1] + 1)

        #Check if the neighbors are in the graph
        #Append them if so
        if north in graph:
            graph[coord].append(north)
        if south in graph:
            graph[coord].append(south)
        if west in graph:
            graph[coord].append(west)
        if east in graph:
            graph[coord].append(east)

def transpose_nodes(image):
    width, height = image.size

    graph = {}
    for row in range(0, height):
        for col in range(0, width):

            # Coordinate of the
            coord = (col, row)
            color = image.getpixel(coord)

            # Check if the coordinate is white
            if color == (255, 255, 255):
                #Add an empty list to the coordinates
                graph[coord] = []

    return graph


