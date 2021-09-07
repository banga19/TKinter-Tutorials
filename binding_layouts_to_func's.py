from tkinter import *
root = Tk()

# method 1 and the best option  and it prints on the terminal not on the window
def PrintName():
    print("Hello My name is BANGA")

button_1= Button(root,text="Print it", command=PrintName )
button_1.pack()


root.mainloop()




