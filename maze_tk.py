import tkinter as tk
import random
import time



# program variables
SCREEN_WIDTH =800
SCREEN_HEIGHT = 800

RECT_WIDTH = 50
RECT_HEIGHT = 50

RECT_NUM_HOR = int(SCREEN_WIDTH/RECT_WIDTH)
RECT_NUM_VER = int(SCREEN_HEIGHT/RECT_HEIGHT)
matrix_size = RECT_NUM_VER * RECT_NUM_HOR

print(RECT_NUM_HOR, RECT_NUM_VER)

rect_array = []
stack = []
current_cell = None
current_cell_index = 8+8*16




# functions for going in each direction

def move_top(current_pos = current_cell_index):
    if current_pos - RECT_NUM_HOR >= 0:
        return current_pos - RECT_NUM_HOR
    else:
        return current_pos

def move_bottom(current_pos):
    if current_pos + RECT_NUM_HOR < matrix_size:
        return current_pos + RECT_NUM_HOR
    else:
        return current_pos

def move_left(current_pos):
    if current_pos % RECT_NUM_HOR != 0:
        return current_pos - 1
    else:
        return current_pos

def move_right(current_pos):
    if (current_pos + 1) % RECT_NUM_HOR != 0:
        return current_pos + 1
    else:
        return current_pos













# Creating the main window
window = tk.Tk()

# Creating the Canvas widget
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()




# Cell class 
class Cell:

    def __init__(self, x:int, y:int, canvas:tk.Canvas):

        self.walls = {'top':True, 'left': True, 'right': True, 'bottom':True}
        self.visited = False
        self.x_coord = x
        self.y_coord = y

        # For top line
        self.top = canvas.create_line(x, y, x+RECT_WIDTH, y)
        # for left line
        self.left = canvas.create_line(x, y, x, y+RECT_HEIGHT)
        # for bottom line
        self.bottom = canvas.create_line(x, y+RECT_HEIGHT, x+RECT_WIDTH, y+RECT_HEIGHT)
        # for right line
        self.right = canvas.create_line(x+RECT_WIDTH, y, x+RECT_WIDTH, y+RECT_HEIGHT)

        # for the rectangle between the lines
        self.rectangle = canvas.create_rectangle(x, y, x+RECT_WIDTH, y+RECT_HEIGHT, fill='lightblue')


    def set_current(self, curr):
        if curr:
            canvas.itemconfig(self.rectangle, fill="red")
        else:
            canvas.itemconfig(self.rectangle, fill="lightblue")
        window.update()
        

    def __str__(self):
        return "Coordinates: "+ str(self.x_coord)+ ', ' + str(self.y_coord)










dir = ''
rand_coord = 0



def generate_maze():
    global current_cell_index
    time.sleep(2)
    

    dir = random.choice(['left', 'right', 'top', 'bottom'])
    if (dir=='left'):
        current_cell_index = move_left(current_cell_index)

    elif(dir=='right'):
        current_cell_index = move_right(current_cell_index)
    elif(dir=='top'):
        current_cell_index = move_top(current_cell_index)
    else:
        current_cell_index = move_bottom(current_cell_index)
    
    # Reseting the last curernt cell to default
    rect_array[current_cell_index].set_current(True)
    # Setting the next cell to the current
    print(current_cell_index)

    print('current cell is blah blah: '+ str( rect_array[current_cell_index]))
    # current_cell.set_current(True)
    
    window.update()
    window.after(10, generate_maze)



































# starting coordinates
x, y = 0, 0
# intial setup 
for i in range(RECT_NUM_VER):
   
    for j in range(RECT_NUM_HOR):
        
        cell = Cell(x, y, canvas)
        print(cell)
        rect_array.append(cell)
        x += RECT_WIDTH
    y += RECT_HEIGHT
    x = 0


# setting the current cell to the top left
current_cell_index = 8+8*16
print('curent index: '+ str(current_cell_index))

current_cell = rect_array[current_cell_index]
print('coordinates '+ str(current_cell))
current_cell.set_current(True)
# generate_maze()

















def key_pressed(event):
    generate_maze()






# Bind the keypress event to the space key
window.bind("<space>", key_pressed)

# Set the focus to the window so that it receives key events
window.focus_set()



# Start the Tkinter event loop
window.mainloop()
