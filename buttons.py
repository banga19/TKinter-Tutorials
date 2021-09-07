from tkinter import *
root = Tk()

topFrame = Frame(root)
topFrame.pack() # makes the above line to appear
bottomFrame = Frame(root)
bottomFrame.pack()  # makes the above line to appear


button1 = Button(topFrame,text="click me",  fg="red")
button2 = Button(topFrame, text="click me",  fg="orange")
button3 = Button(topFrame, text="click me",  fg="black")
button4 = Button(bottomFrame, text="click me",  fg="brown")

# fg means color

button1.pack(side=LEFT)  # makes the button1 to appear
button2.pack(side=RIGHT)  # makes the button2 to appear
button3.pack()  # makes the button3 to appear
button4.pack()  # makes the button4 to appear

root.mainloop()