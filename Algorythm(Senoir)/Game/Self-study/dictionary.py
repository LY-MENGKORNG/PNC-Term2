from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("Dictionary")
root.configure(bg="black")

#Create label
Label(root, text="Enter your word", bg="black", fg="white", font="arial, 20") .grid(row=0, column=0, sticky=W)

#Text input
text =Entry(root, width=30, bg="white")
text.grid(row=2, column=0, sticky=W)

#Enter button
def click():
    # global output
    entered_text=text.get() #this will collect all text from text input
    text.delete(0, "end")
    try:
        definition=my_dictionary[entered_text]
    except:
        definition="Sorry we have this word's definition"
    output.insert(END, definition)

    
    
    
    
Button(root, text="Search", width=6, command=click) .grid(row=3, column=0, sticky=W)
# Button(root, text="Clear", width=6, command=Cleartext) .grid(row=7, column=0, sticky=S)

#Definition Label
Label(root, text="Definition", bg="black", fg="white", font="arial, 20") .grid(row=4, column=0, sticky=W)


#Definition box
output= Text(root, width=50, height=10, bg="white", wrap=WORD, font=("arial", 20))
output.grid(row=5, column=0,  sticky=W)


#Words difinitions
my_dictionary= {
    "Visal": "good person, the best person in the world, good man"
}










root.mainloop()
