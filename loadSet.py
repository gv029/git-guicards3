from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

#dev branch
root = Tk()

root.filename = filedialog.askopenfilename(title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))




root.mainloop()
