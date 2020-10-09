
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#dev branch
terms=[]
defs=[]
dict={}

def add():

    terms.append(termEntry.get())
    defs.append(defEntry.get())

    termEntry.delete(0, END)
    defEntry.delete(0, END)



def done():

    for i in range(len(terms)):
        dict[terms[i]] = defs[i]



    filename = filedialog.asksaveasfile(title="Save file", mode="w",defaultextension=".txt")
    name=filename.name

    f = open(name,"w+")
    f.write(str(dict))
    f.close()



root = Tk()

termEntry = Entry(root, width=20)
termEntry.pack()

defEntry = Entry(root, width =50)
defEntry.pack()

addButton = Button(root,text="Add",command=add)
addButton.pack()

doneButton = Button(root,text="Done",command=done)
doneButton.pack()


root.mainloop()
