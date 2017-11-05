import PIL.Image as Image
import sys;

import BasicNodeTrasposer
import BreadthFirstSearchSolver
import PaintImage

sys.setrecursionlimit(10000)

image = Image.open("medmaze.bmp")
image = image.convert('RGB')

width, height = image.size;

#Get the graph
graph = BasicNodeTrasposer.get_graph(image)

#Get endpoints
start, end = BasicNodeTrasposer.getEnds(image)

#Create a queue
queue = BreadthFirstSearchSolver.get_queued_nodes(graph, start, end);

PaintImage.paint(image, queue, "new.bmp")