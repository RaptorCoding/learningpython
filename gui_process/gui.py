from tkinter import *

def button_press():
    pass

def equals():
    pass

def clear():
    pass

root = Tk()
root.geometry("300x400")
root.title("Calculator")

button = Button(root, height=3,)

equationtext = ""
equation_label = StringVar()

label = Label(root, textvariable=equation_label, font=('Comicsans'))

root.mainloop()