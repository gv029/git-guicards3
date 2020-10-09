from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()

mySet = filedialog.askopenfile(mode="r")
info = mySet.read()
print(info)

infoLabel = 

root.mainloop()
