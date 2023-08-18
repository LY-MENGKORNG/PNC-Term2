import tkinter as tk

# ---------------------------------------------------------------------------
# Global data
# ---------------------------------------------------------------------------
score = 0

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def onClickOnAdd(event) :
    setScore(score + 1)

def onClickOnMinus(event) :
    setScore(score - 1)
    
def setScore(newScore) :
    # 1 - Update the score
    global score
    score = newScore
    
     # 2 - Update the label with the new score
    canvas.itemconfig(scoreLabel, text=score)



# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
root = tk.Tk()
root.geometry("300x200")
canvas = tk.Canvas(root)

# Create the score label
scoreLabel = canvas.create_text(120, 50, text=score, font=('consolas', 50, 'bold'))


# Create the remove label
minusLabel = canvas.create_text(50, 100, text='Minus', tags="minusLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("minusLabel","<Button-1>", onClickOnMinus)

# Create the add label
addLabel = canvas.create_text(200, 100, text='Add', tags="addLabel", font=('consolas', 24, 'bold'))
canvas.tag_bind("addLabel","<Button-1>", onClickOnAdd)


canvas.pack(expand=True, fill='both')
root.mainloop()
