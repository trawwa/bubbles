from random import *
from tkinter import *
import tkinter


size = 1280
window = Tk()
window.title("bubbles")
canvas = Canvas(window, width=size, height=size)
canvas.pack()
diapason = 0


while True:
    colors = choice(['aqua', 'blue', 'green', 'yellow', 'orange', 'maroon', 'pink', 'purple', 'red', 'lime', 'indigo'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
    window.update()
    diapason += 1