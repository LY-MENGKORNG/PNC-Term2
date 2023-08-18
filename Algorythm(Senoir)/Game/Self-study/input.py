
from tkinter import *
from unittest import result

root=Tk()
root.title("Hello")
root.geometry("400x400")

# <---Main program---->

# Label
l=Label(root, text="Enter your name")
l.pack()

# For input 
e= Entry(root,borderwidth=10)
e.pack()
# e.insert(0, "Enter your name")        #This is similar to placeholder

def myName():
    global result              
    me="Hello "+ e.get() +". What is your name?"
    result=Label(root, text=me)
    result.pack()
    enterButton["stat"]=DISABLED
    e.delete(0, "end")                  #Delete input after click on button
    
def deleteName():
    result.destroy()
    enterButton["stat"]=NORMAL
    # if result.winfo_exists()==1:    #Result of winfo_exists is: 1
    #     result.destroy()
    #     myButton["stat"]=NORMAL

enterButton=Button(root, text="Enter", command=myName)
enterButton.pack()
# root.bind("<Return>", myName)               #Another to enter button

deleteButton=Button(root, text="Delete", command=deleteName)
deleteButton.pack()


# <---Display-->
root.mainloop()