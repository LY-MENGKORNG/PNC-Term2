from tkinter import *
from turtle import width

root=Tk()
root.geometry("600x600")
root.title("Dictionary")
root.configure(bg="black")

# <---Main program---->
label=Label(root, text="Enter the word", font=("arial", 20), bg="black", fg="white") .grid(row=1, column=0, sticky=W)

#Functions
def click():
    entered_text=input.get()
    input.delete(0, "end")
    try:
        definition= my_dictionary[entered_text]
    except:
        definition= "No definition of this word"
    output.insert("end",definition)


#Text input
input=Entry(root, width=30) 
input.grid(row=2, column=0, sticky=W)

#Button enter
button=Button(root, text="Enter", command=click) .grid(row=3,column=0,sticky=W)

#Definiton label
label=Label(root,height=3, text="Definition:", font=("arial", 20), bg="black", fg="white") .grid(row=6, column=0, sticky=W)

#Definiton box
output= Text(root, width=50, height=5, bg="white", wrap=WORD, font=("arial", 20))
output.grid(row=7, column=0,  sticky=W)


#Dictionary
my_dictionary={
    "visal": "good persion, special person, the best person in the world", "crush": "that's a person who studid that don't who is loving them."
}

root.mainloop()