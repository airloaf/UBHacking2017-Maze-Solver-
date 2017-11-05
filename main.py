import PIL.Image as Image
import PIL.ImageTk as ImageTk

import BreadthFirstSearchSolver
import AStarSolver
import PaintImage

import tkinter as tk


root = tk.Tk()
root.title("Maze Solver")
root.resizable(0, 0)

select_button = tk.Button(root, text="Select Image")
start_button = tk.Button(root, text="Start")

input_label = tk.Label(root, text="No Image Selected")
paint_label = tk.Label(root, text="Path Paint")
status_label = tk.Label(root, text="No Task")
out_label = tk.Label(root, text="Save Name:")

name_entry = tk.Entry(root)

choice = tk.IntVar()

rainbow_radio = tk.Radiobutton(root, text="rainbow", value=1, variable=choice)
gradient_radio = tk.Radiobutton(root, text="gradient", value=2, variable=choice)

select_button.grid(row=0, column=0, columnspan=2)
paint_label.grid(row=0, column=2, columnspan=2)

input_label.grid(row=1, column=0, columnspan=2)
rainbow_radio.grid(row=1, column=2, columnspan=2)

out_label.grid(row=2, column=0, sticky=tk.W)
name_entry.grid(row=2, column=1)
gradient_radio.grid(row=2, column=2, columnspan=2)

start_button.grid(row=3, column=0, columnspan=2)
status_label.grid(row=3, column=2, columnspan=2)

root.mainloop()

'''
image = Image.open("4096x4096.bmp")
image = image.convert('RGB')

#get the queue of nodes
#queue = BreadthFirstSearchSolver.get_nodes(image)
queue = AStarSolver.get_nodes(image)

PaintImage.paint(image, queue, "new.bmp")
'''