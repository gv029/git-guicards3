
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

terms=[]
defs=[]
dict={}

def loadSet():
    showSet = Toplevel()
    showSet.geometry("500x300")
    defLabel = Label(showSet, text="test")
    defLabel.pack()

    name = root.filename = filedialog.askopenfilename(title="Select A File", filetypes=((".txt files", "*.txt"),("All files", "*.*")))



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

#function that opens a window to create a new set of flashcards
def openNew():
    newSet = Toplevel()
    newSet.title("Create a new set")

    global termEntry
    global defEntry

    termEntry = Entry(newSet, width=20)
    termEntry.pack()

    defEntry = Entry(newSet, width =50)
    defEntry.pack()

    addButton = Button(newSet,text="Add",command=add)
    addButton.pack()

    doneButton = Button(newSet,text="Done",command=done)
    doneButton.pack()


#root window stuff
root = Tk()

root.geometry("300x300")

loadButton = Button(root,text="Load",command=loadSet)
loadButton.pack()

newButton = Button(root,text="Create a new set",command=openNew)
newButton.pack()

quizButton = Button(root,text="Quiz!")
quizButton.pack()




root.mainloop()
