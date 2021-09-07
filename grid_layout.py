# making a simple login area using 2 labels and 1 button(optional button)


from tkinter import *
root = Tk()

# first create a label
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

# create a text area for he labels above

entry_1 = Entry(root)
entry_2 = Entry(root)

# then place them wherever you want them to be on the display  window named root


label_1.grid(row=0,sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0 , column=1)
entry_2.grid(row=1, column=1)

# creating a keep me logged in checkbox .
# first create any variable and inside it use "Checkbutton" and display it on
# the main window.

banga = Checkbutton(root, text= "keep me logged in" )
banga.grid(columnspan=2)

# optional 'SUBMIT' button

button = Button(root, text="SUBMIT", fg="violet", bg="teal", )
button.grid(row=3, column=1)


# .grid() is better for positioning of widgets than .pack()

root.mainloop()