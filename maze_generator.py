import pygame
import random



# program variables
SCREEN_WIDTH =800
SCREEN_HEIGHT = 800

RECT_WIDTH = 50
RECT_HEIGHT = 50

RECT_NUM_HOR = int(SCREEN_WIDTH/RECT_WIDTH)
RECT_NUM_VER = int(SCREEN_HEIGHT/RECT_HEIGHT)
matrix_size = RECT_NUM_VER * RECT_NUM_HOR

print(RECT_NUM_HOR, RECT_NUM_VER)

rectangles = []
stack = []
current_cell = None
current_cell_index = 8+8*16
prev = 0

backtracking = False


dir = -1


def increase_color_gradient(color, increment):
    """
    Increases the color gradient of a given color.

    Args:
        color (pygame.Color): The color to increase the gradient.
        increment (int): The amount to increment each color component.

    Returns:
        pygame.Color: The updated color with increased gradient.
    """
    new_color = pygame.Color(color.r + increment, color.g + increment, color.b + increment)
    return new_color


# functions for going in each direction
def move_top(current_pos):
    
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







# Cell class 
class Cell:

    def __init__(self, x:int, y:int, i):

        self.walls = {'top':True, 'left': True, 'right': True, 'bottom':True}
        self.visited = False
        self.x_coord = x
        self.y_coord = y
        self.color = 'yellow'
        self.index = i
        self.left_line = 5
        self.rigth_line = 5
        self.top_line = 5
        self.bottom_line = 5

        

        # For top line
        # self.top = pygame.Line(x, y, x+RECT_WIDTH, y)
        # # for left line
        # self.left = pygame.Line(x, y, x, y+RECT_HEIGHT)
        # # for bottom line
        # self.bottom = pygame.Line(x, y+RECT_HEIGHT, x+RECT_WIDTH, y+RECT_HEIGHT)
        # # for right line
        # self.right = pygame.Line(x+RECT_WIDTH, y, x+RECT_WIDTH, y+RECT_HEIGHT)

        # for the rectangle between the lines
        self.rectangle = pygame.Rect(x, y, x+RECT_WIDTH, y+RECT_HEIGHT )


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle, border_radius=10)
        pygame.draw.line(screen, 'lightblue',( self.x_coord, self.y_coord),( self.x_coord+RECT_WIDTH, self.y_coord), self.top_line)
        pygame.draw.line(screen, 'lightblue',( self.x_coord, self.y_coord),( self.x_coord, self.y_coord+RECT_WIDTH), self.left_line)
        pygame.draw.line(screen, 'lightblue',( self.x_coord, self.y_coord+RECT_WIDTH),( self.x_coord+RECT_WIDTH, self.y_coord+RECT_WIDTH), self.bottom_line)
        pygame.draw.line(screen, 'lightblue',( self.x_coord+RECT_WIDTH, self.y_coord),( self.x_coord+RECT_WIDTH, self.y_coord+RECT_WIDTH), self.rigth_line)


    def update(self, prev):
        if self.walls['left'] == False:
             self.left_line = 0
             prev.right_line = 0
        if self.walls['right'] == False:
             self.rigth_line = 0
             prev.left_line = 0
        if self.walls['top'] == False:
             self.top_line = 0
             prev.bottom_line = 0
        if self.walls['bottom'] == False:
             self.bottom_line = 0
             prev.top_line = 0

        pass
        

    def set_current(self, bool):
        if bool:
            self.color = 'red'
        else:
            self.color = 'purple'


        self.visited = True





    def __str__(self):
        return "Coordinates: "+ str(self.x_coord)+ ', ' + str(self.y_coord)



# starting coordinates
x, y = 0, 0
# intial setup 
for i in range(RECT_NUM_VER):

    for j in range(RECT_NUM_HOR):
        
        cell = Cell(x, y, j + i*RECT_NUM_HOR)
        print(cell)
        rectangles.append(cell)
        x += RECT_WIDTH
    y += RECT_HEIGHT
    x = 0




















# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True




current_cell = rectangles[current_cell_index]
stack.append(current_cell)
stack.append(current_cell)
# def back_track():
#     for i in range(len(stack)):
#         last = stack.pop()
#         list = [move_left(last.index), move_top(last.index), move_bottom(last.index), move_right(last.index)]
#         for dir in list:
#             if rectangles(dir).visited:
#                 continue
#             else:
#                 current_cell_index = last.index
#                 current_cell = last
#                 stack.append(last)
def back_track():
    global current_cell_index, current_cell, backtracking
    print('length is ' + str(len(stack)))
    current_cell = stack.pop()
    current_cell_index = current_cell.index
    print(str(current_cell_index))
    if rectangles[move_left(current_cell_index)].visited == False or  rectangles[move_top(current_cell_index)].visited == False or  rectangles[move_bottom(current_cell_index)].visited ==False or  rectangles[move_right(current_cell_index)].visited == False:
        backtracking = False



# def next_rectangle():
#     bool = True
#     initial_value = current_cell_index
#     list = [move_left(current_cell_index), move_top(current_cell_index), move_bottom(current_cell_index), move_right(current_cell_index)]
#     for x in range(4):
#         if len(list) == 0:
#             back_track()
        
#         dir = random.choice(list)
#         # remember that the functions return the intial value if the array is out of index
#         if  rectangles[dir].visited :
#             bool = True
#             # list.remove(dir)
#         else:

#             bool = False
#             return dir
        
#     return 0






while running:
    # poll for events
    # pygame.QUIT 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the rectangles
    # for rectangle in rectangles:
    #     rectangle.update(dir)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the rectangles
    for rectangle in rectangles:
        rectangle.draw(screen)



    # RENDERING
    # stack.append(current_cell)
    current_cell.set_current(False)
    list = [ move_top(current_cell_index), move_left(current_cell_index), move_right(current_cell_index), move_bottom(current_cell_index)]

    while True:
        if len(list) == 0:
            backtracking = True
            back_track()
            break
        prev = current_cell_index
        current_cell_index = random.choice(list)
        
        # remember that the functions return the intial value if the array is out of index
        if  rectangles[current_cell_index].visited :
            list.remove(current_cell_index)
        elif rectangles[current_cell_index].visited == False:
            i = list.index(current_cell_index)
            if i == 0:
                stack[len(stack)-1].walls = {'top':False, 'left': True, 'right': True, 'bottom':True}
            elif i == 1:
                 stack[len(stack)-1].walls = {'top':True, 'left': False, 'right': True, 'bottom':True}
            elif i == 2:
                stack[len(stack)-1].walls = {'top':True, 'left': True, 'right': False, 'bottom':True}
            elif i == 3:
                stack[len(stack)-1].walls = {'top':True, 'left': True, 'right': True, 'bottom':False}

            stack[len(stack)-1].update(stack[len(stack)-2])
            break
        


    
    # current_cell_index = next_rectangle()

    # current_cell.set_current(False)
    prev = current_cell



    current_cell = rectangles[current_cell_index]

    if not backtracking:
    
        stack.append(current_cell)
    # if current_cell_index in list:

        # current_cell.update(list.index(current_cell_index), prev)
    current_cell.set_current(True)
    
    

    # dir = random.choice(['left', 'right', 'top', 'bottom'])
    # if (dir=='left'):
    #     current_cell_index = move_left(current_cell_index)

    # elif(dir=='right'):
    #     current_cell_index = move_right(current_cell_index)
    # elif(dir=='top'):
    #     current_cell_index = move_top(current_cell_index)
    # else:
    #     current_cell_index = move_bottom(current_cell_index)
    
    # current_cell = rectangles[current_cell_index]
    # current_cell.


































    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(2)  # limits FPS to 60

pygame.quit()