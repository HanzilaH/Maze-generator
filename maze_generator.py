import pygame
import random

# info: This program uses the depth first algorithm to generate mazes
# the surrounding blocks are checked if they are unvisited
# then a movement is made in that direction and the walls are removed
# if all the surrounding blocks are already visited then the rectangle backtracks 
# after generating the maze the rectangle always moves to the initial position
# the class Rect is used to represent each of the block of rectangle using it found surrounding lines
# pygame Rectangles dont allow me to uses custom border length for a rectangle thats why the class Rect is necessary


# program variables
SCREEN_WIDTH =800
SCREEN_HEIGHT = 800

# you can edit these variables to produce a maze of any number of rectangles
RECT_WIDTH = 50
RECT_HEIGHT = 50

RECT_NUM_HOR = int(SCREEN_WIDTH/RECT_WIDTH)
RECT_NUM_VER = int(SCREEN_HEIGHT/RECT_HEIGHT)
matrix_size = RECT_NUM_VER * RECT_NUM_HOR




# this array is for all of the rectangles
rectangles = []
# this array is to keep track of the visited rectangles
stack = []


current_rect = None
# you can reset the current index to change the initial position of the algorithm
current_rect_index = 0


backtracking = False
# this is used for the main loop
running = True








# rect class 
class Rect:
    '''Class for each of the rectangle block displayed on screen including the four lines surrounding the rectangles'''

    def __init__(self, x:int, y:int, i):

        self.walls = {'top':True, 'left': True, 'right': True, 'bottom':True}
        self.visited = False
        self.x_coord = x
        self.y_coord = y
        self.color = 'darkgreen'
        self.index = i

        # These are the length of each of the four lines
        # Not much used
        self.left_line = 1
        self.rigth_line = 1
        self.top_line = 1
        self.bottom_line = 1

        # for the rectangle between the lines
        self.rectangle = pygame.Rect(x, y, x+RECT_WIDTH, y+RECT_HEIGHT )


    def draw(self, screen):
        '''Draws the main rectangle and draws all the four walls depending on the value of booleans'''
        pygame.draw.rect(screen, self.color, self.rectangle)
        # For top line
        if self.walls['top'] == True:
            pygame.draw.line(screen, 'black',( self.x_coord, self.y_coord),( self.x_coord+RECT_WIDTH, self.y_coord), self.top_line)
         # # for left line
        if self.walls['left'] == True:
            pygame.draw.line(screen, 'black',( self.x_coord, self.y_coord),( self.x_coord, self.y_coord+RECT_WIDTH), self.left_line)
         # # for bottom line
        if self.walls['bottom']== True:
            pygame.draw.line(screen, 'black',( self.x_coord, self.y_coord+RECT_WIDTH),( self.x_coord+RECT_WIDTH, self.y_coord+RECT_WIDTH), self.bottom_line)
         # # for right line
        if self.walls['right'] == True:
            pygame.draw.line(screen, 'black',( self.x_coord+RECT_WIDTH, self.y_coord),( self.x_coord+RECT_WIDTH, self.y_coord+RECT_WIDTH), self.rigth_line)


        

    def set_current(self, bool):
        '''Use this function to reset colors for the current rectangle and the other rectangles'''
        if bool:
            self.color = 'red'
        else:
            self.color = 'lightgreen'


        self.visited = True

    def __str__(self):
        '''return the string with the coordinates of the rectangle'''
        return "Coordinates: "+ str(self.x_coord)+ ', ' + str(self.y_coord)



# functions for going in each direction
# All four of these function return the same index if its out of range
# Each return the 1D array INDEX for the next rectangle
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





# starting coordinates
x, y = 0, 0
# intial setup 
# adds the rectangle classes to the array
for i in range(RECT_NUM_VER):

    for j in range(RECT_NUM_HOR):
        
        rect = Rect(x, y, j + i*RECT_NUM_HOR)
        # print(rect)
        rectangles.append(rect)
        x += RECT_WIDTH
    y += RECT_HEIGHT
    x = 0




















# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()





current_rect = rectangles[current_rect_index]


def back_track():
    '''Use the last entry of the stack to set the current rectangle
    This function also performs a mini check to see if any one of the sides of the current rectangle is unvisited
    Consequently it sets the value of backtracking boolean to false'''
    global current_rect_index, current_rect, backtracking



    # this if condition is only here to prevent the window from closing in the end
    if len(stack)> 0:
        current_rect = stack.pop()



    current_rect_index = current_rect.index

    if rectangles[move_left(current_rect_index)].visited == False or  rectangles[move_top(current_rect_index)].visited == False or  rectangles[move_bottom(current_rect_index)].visited ==False or  rectangles[move_right(current_rect_index)].visited == False:
        backtracking = False



def remove_walls(current, next):
    '''Simple mathematics to calculate the difference in x and y values
    Then difference is used to determine this walls from each rectangle to remove'''

    # I was making a major blunder by reversing the subtractions 
    x_diff = next.x_coord - current.x_coord
    y_diff = next.y_coord - current.y_coord
    
    if x_diff == RECT_WIDTH:  # Moving to the right
        current.walls['right'] = False
        next.walls['left'] = False
    elif x_diff == -RECT_WIDTH:  # Moving to the left
        current.walls['left'] = False
        next.walls['right'] = False
    elif y_diff == RECT_HEIGHT:  # Moving downwards
        current.walls['bottom'] = False
        next.walls['top'] = False
    elif y_diff == -RECT_HEIGHT:  # Moving upwards
        current.walls['top'] = False
        next.walls['bottom'] = False







while running:
    # for the quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    # to clear the screen after every frame
    screen.fill((0, 0, 0))

    



    # RENDERING

    # at the start of each loop current rectangle is reset
    current_rect.set_current(False)



    # remember that the functions return the intial value if the array is out of index
    li = [ move_top(current_rect_index), move_left(current_rect_index), move_right(current_rect_index), move_bottom(current_rect_index)]
    
    # this loop runs for 4 times at most for each of the options on the list
    # first chooses a random direction then checks whether that was been visited if yes then the index is removed from the list
    # if all the four direction are visited then it does backtracking (one rectangle per main loop)
    # NOTE: initially i struggled to understand how backtracking worked with the frames
    # but then what i did is we only backtrack one square for each Main loop
    while True:
        if len(li) == 0:
            backtracking = True
            back_track()
            break
       
        current_rect_index = random.choice(li)
        
        
        if  rectangles[current_rect_index].visited :
            li.remove(current_rect_index)
        elif rectangles[current_rect_index].visited == False:
            break


    
    


    # to set a ref to next rectangle which can be used later
    next_rect = rectangles[current_rect_index]
    # to remove the walls between the next and the current rectangle
    remove_walls(current_rect, next_rect)
    current_rect = next_rect


    # print('current i: '+ str(current_rect.index)+ ' next i '+ str(next_rect.index))


    # each current rectangle is only added to the stack if we are not backtracking
    if not backtracking:
        stack.append(current_rect)


    current_rect.set_current(True)
    

    
    # Drawing the rectangles
    for rectangle in rectangles:
        rectangle.draw(screen)
    


















    pygame.display.flip()

    clock.tick(40)  # limits FPS

pygame.quit()