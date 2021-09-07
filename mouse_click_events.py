from tkinter import *

# when you click the left mouse button it displays the "left" on the console
# the same happens to when you click the right and middle mouse button 

root = Tk()


def RightClick(event):
    print("Right")


def LeftClick(event):
    print("Left")


frame = Frame(root, width=500, height=300)

frame.bind("<button-1>", RightClick)
frame.bind("<button-2>", LeftClick)
frame.pack()

root.mainloop()
