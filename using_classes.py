# using classes to build a regular GUI  and  regular widgets

# master = root = where the window is and where the widgets and buttons will be displayed  will be displayed
# __init__(self) means to start  and it is a function that stores all the parameters below
from tkinter import *


class Banga:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack() # this means to make it be displayed on the window

        self.printButton = Button(frame, text="Tap Me", command=self.printMessage)
        self.printButton.pack(side=LEFT)  # this means to make the above button  appear  on the window

        self.quitButton = Button(frame, text="QUIT", command=frame.quit)
        self.quitButton.pack(side=LEFT) # this means to make the above button to appear on the above window

    def printMessage(self,):
        print("WOW, this Actually worked for me ")


root = Tk()


ban = Banga(root)

root.mainloop()
     




