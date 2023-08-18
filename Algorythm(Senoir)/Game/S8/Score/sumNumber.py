#  IMPORTS
import tkinter as tk

#  CONSTANTS
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# squareSize = #choose the appropriate size of the squares
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)


 #------------Main program-----------
number=0
def sumNb(event):
    global number
    number+=1
    print(number)
def score(event):
    global number
    number+=1
    print("score: ",number)
    
        
root.bind("<a>", sumNb)
root.bind("<b>", score)



#------------------Display------------
root.mainloop()