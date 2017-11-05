import PIL.Image as Image

def bfs(graph, visited, queue, parent):
    #Get the current node
    current = queue[0]
    queue.pop(0)
    visited[current] = True

    #Get the neighbors
    neighbors = graph[current]

    #For each neighbor of the node
    for neighbor in neighbors:
        #Check if it has not been visited or queued
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
            parent[neighbor] = current

    #If there is more queued, then BFS more
    if len(queue) > 0:
        bfs(graph, visited, queue, parent)
    else:
        return

def get_nodes(image):

    #Create a graph
    graph = create_graph(image)

    #Get the end points
    start, end = get_ends(image)

    #BFS Helpers
    visited = {}
    queue = []
    parent = {}

    queue.append(start)
    parent[start] = None

    bfs(graph, visited, queue, parent)

    nodeQueue = []

    par = end
    while par != None:
        nodeQueue.insert(0, par)
        par = parent[par]

    return nodeQueue

'''
Get the entrances and exits of images
'''

def get_ends(image):
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

'''
Transpose the image into a graph
'''

def create_graph(image):
    graph = transpose_nodes(image)
    get_neighbors(graph)
    return graph

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