import PIL.Image as Image

import BasicNodeTrasposer
import BreadthFirstSearchSolver

image = Image.open("bigmaze.bmp")
image = image.convert('RGB')

width, height = image.size;

graph = BasicNodeTrasposer.get_graph(image)
print("Created graph")

start, end = BasicNodeTrasposer.getEnds(image)

queue = BreadthFirstSearchSolver.get_queued_nodes(graph, start, end);
print("did BFS")

pix = image.load()
for i in queue:
    pix[i[0], i[1]] = (0, 255, 0)

image.save("new.bmp")