from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import re

terms =['Click next to begin']
definitions = ['']
dict = {}

#dev branch
root = Tk()
root.geometry("500x300")

#creating a function that a button will utilized to change the term

x=0
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


#GUI
nextButton = Button(root, text="Next", command=nextTerm)
nextButton.pack()
displayLabel1 = Label(root,text=te)
displayLabel1.pack()
displayLabel2 = Label(root,text=de)
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





#print(terms)
#print('----')
#print(definitions)
#print("------")
#print(dict)


root.mainloop()
