from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
              # these numbers are coordinates that are written in (X,y) form
blackLine = canvas.create_line(0, 1, 100, 60, fill="black")
redLine = canvas.create_line(0, 100, 100, 60, fill="red")
rectangle = canvas.create_rectangle(25, 25, 150, 60, )

root.mainloop()