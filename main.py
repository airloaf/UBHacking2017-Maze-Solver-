import PIL.Image as Image
import sys;

import BreadthFirstSearchSolver
import AStarSolver

import PaintImage

sys.setrecursionlimit(5000)

image = Image.open("small.bmp")
image = image.convert('RGB')

#get the queue of nodes
#queue = BreadthFirstSearchSolver.get_nodes(image)
queue = AStarSolver.get_nodes(image)

PaintImage.paint(image, queue, "new.bmp")