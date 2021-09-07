from tkinter import *
root = Tk()


one = Label(root, text="banga" , bg="white" , fg="black")
one.pack()

two = Label(root, text="Mariam" , bg="purple" , fg="white")
two.pack(fill=X)

three = Label(root, text="Amadou", bg="red", fg="white")
three.pack()

four = Label(root, text="Nikitta", bg="black", fg="white")
four.pack(side=LEFT, fill=Y)

root.mainloop()

# (fill=X)Means that the label extends and stretches on the x-axis
# the same above goes when you replace x with y but it goes to the y-axis