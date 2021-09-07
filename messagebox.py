from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("WINDOW TITLE", "Did you know humans are immortal") # showing some information
answer = tkinter.messagebox.askquestion("banga", "do you like fish?", ) # asking a yes or no question

if answer == "yes":
    print("You are awesome")
else:
    print("Good luck ")

root.mainloop()

