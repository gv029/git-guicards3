
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import re


terms=[]
defs=[]
dict={}
x=0

def loadSet():

    terms =['Select file and click next to begin']
    definitions = ['']
    dict = {}


    te = terms[x]
    de = definitions[x]
    def nextTerm():
        global x
        x = x+1
        if x >= len(terms):
            te = "You have reached the end of the list"
            de = ""
            displayLabel1.configure(text=te)
            displayLabel2.configure(text=de)
        else:
            te = terms[x]
            de = definitions[x]
            displayLabel1.configure(text=te)
            displayLabel2.configure(text=de)

    window = Toplevel()
    window.geometry("500x300")
    window.title("Load Set")

    #GUI
    nextButton = Button(window, text="Next", command=nextTerm)
    nextButton.pack()
    displayLabel1 = Label(window,text=te)
    displayLabel1.pack()
    displayLabel2 = Label(window,text=de)
    displayLabel2.pack()



    name = root.filename = filedialog.askopenfilename(title="Select A File", filetypes=((".txt files", "*.txt"),("All files", "*.*")))
    f = open(name, 'r')
    text = f.read()

    #using regex to split where there are single quotes, creating an list called "text" with all the terms and definitions
    regex = re.compile(r"'[^']*'")
    text = [x.strip("'") for x in regex.findall(text)]

    #populating the terms and definitions arrays so the terms and definitions are seperate lists
    for index, element in enumerate(text):
        if index%2 == 0:
            terms.append(element)
        else:
            definitions.append(element)

    #populating a dictionary based off the previous two lists
    num = len(terms)
    for i in range(num):
        dict[terms[i]] = definitions[i]

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
root.title("Flashcards!")

loadButton = Button(root,text="Load",command=loadSet)
loadButton.pack()

newButton = Button(root,text="Create a new set",command=openNew)
newButton.pack()

quizButton = Button(root,text="Quiz!")
quizButton.pack()




root.mainloop()
