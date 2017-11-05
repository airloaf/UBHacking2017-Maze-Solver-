import PIL.Image as Image
import BreadthFirstSearchSolver
import AStarSolver
import PaintImage

image = Image.open("small.bmp")
image = image.convert('RGB')

#get the queue of nodes
#queue = BreadthFirstSearchSolver.get_nodes(image)
queue = AStarSolver.get_nodes(image)

PaintImage.paint(image, queue, "new.bmp")
