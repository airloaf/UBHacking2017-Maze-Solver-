import PIL.Image as Image

import AStarSolver
import PaintImage

import os

import threading
import time

import tkinter as tk
from tkinter.filedialog import askopenfilename

RAINBOW_PAINT = 0
GRADIENT_PAINT = 1

file_name = ""
file_save_name = ""
file_paint = RAINBOW_PAINT

def file_select():
    global file_name
    path = os.getcwd()
    old = "\\"
    new = "/"
    path = path.replace(old, new)
    file_name = askopenfilename(initialdir=path, title="Select Maze", filetypes=[("All Files", "*.*")])
    global input_label
    file_name = file_name[len(path)+1:]
    input_label["text"] = file_name


def start():
    global name_entry
    global file_save_name
    file_save_name = name_entry.get()

    threading.Thread(target=solve).start()

def solve():
    global file_name
    global file_save_name
    global file_paint
    global status_label
    global choice

    a = time.time()

    file_save_name = "output/" + file_save_name

    status_label["text"] = "Loading Image ..."
    image = Image.open(file_name)
    image = image.convert('RGB')

    status_label["text"] = "Solving Maze ..."
    queue = AStarSolver.get_nodes(image)

    status_label["text"] = "Painting Image ..."
    if choice.get() == RAINBOW_PAINT:
        PaintImage.paint_rainbow(image, queue, file_save_name + ".bmp")
    else:
        PaintImage.paint_grad(image, queue, file_save_name + ".bmp")

    b = time.time()

    status_label["text"] = ("Done in {:0.2f}".format(b-a) + " seconds")



root = tk.Tk()
root.title("Maze Solver")
root.resizable(0, 0)

select_button = tk.Button(root, text="Select", command=file_select)
start_button = tk.Button(root, text="Start", command=start)
input_label = tk.Label(root, text="No Image Selected")
paint_label = tk.Label(root, text="Path Paint")
status_label = tk.Label(root, text="No Task")
out_label = tk.Label(root, text="Save Name:")
name_entry = tk.Entry(root)

choice = tk.IntVar()
rainbow_radio = tk.Radiobutton(root, text="rainbow", value=0, variable=choice)
gradient_radio = tk.Radiobutton(root, text="gradient", value=1, variable=choice)

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