# creating a drop down menu
# first i created a variable called CONTAINER  of which
# divided them into two sections the will be drop down menus. Inside them there are
# objects relating with the titles above
from tkinter import *

# """"""MAIN MENU"""""
def Converse():
    print("there are converse shoes inside, just look !")


def Soccer():
    print("there is a soccer ball inside, just look!")


def Rugby():
    print("there is a rugby ball inside , just look")


def doNothing():
    print("ok i wont.......")



root = Tk()

CONTAINER = Menu(root)
root.config(menu=CONTAINER)

subMenu = Menu(CONTAINER)
CONTAINER.add_cascade(label="sports Box", menu=subMenu)
subMenu.add_command(label="Soccer ball", command=Soccer)
subMenu.add_command(label="rugby", command=Rugby)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

# adding another drop down menu
editMenu = Menu(CONTAINER)
CONTAINER.add_cascade(label="Shoes", menu=editMenu)
editMenu.add_command(label="converse", command=Converse)

# """"TOOL BAR""""""

toolbar = Frame(root, bg="light green")
butt_1 = Button(toolbar, text="Insert Image", command=doNothing)
butt_1.pack(side=LEFT, )
butt_2 = Button(toolbar, text="PRINT", command=doNothing)
butt_2.pack(side=LEFT, )
toolbar.pack(side=TOP, fill=X)


# """""status bar """""""""

status = Label(root, text="lets do this..,", bd=1, relief=SUNKEN, anchor=W )
status.pack(side=BOTTOM, fill=X)








root.mainloop()
