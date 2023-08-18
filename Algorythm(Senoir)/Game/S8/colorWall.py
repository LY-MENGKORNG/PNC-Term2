import tkinter as tk

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
WINDOW_SIZE = 600
COLORS = ['white', 'black', 'red', 'yellow']

# ---------------------------------------------------------------------------
# Global data
# ---------------------------------------------------------------------------
grid = [[0, 0, 1, 0, 2, 0],
        [0, 0, 1, 0, 0, 0],
        [2, 0, 2, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 2],
        [0, 0, 1, 0, 0, 1]]


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

#
# Get the color name, given the number, by looking in the COLORS list
#
def getColorFor(index):
    return COLORS[index] 

def arrayToDrawing():
    # TODO 
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            canvas.create_rectangle(col*100, row*100, col*100+100, row*100+100, fill=getColorFor(grid[row][col]))

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
root = tk.Tk()
root.geometry("600x600")

frame = tk.Frame()
frame.master.title('From Arrays 2D to Graphics')

canvas = tk.Canvas(root)

# create the grid
arrayToDrawing()


canvas.pack(expand=True, fill='both')
root.mainloop()

