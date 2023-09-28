import random
import pprint
import tkinter as tk

BACKGROUND = 0
SNAKE = 1
FRUIT = 2
LEFT = 0 
RIGHT = 1
UP = 2
DOWN = 3
#---------------------------------------------

width = 40
height = 30
cr = 10
color_frame = []
length = 10
direct = RIGHT
root = None
head = (length - 1, 0)
tail = (0, 0)
stack = [RIGHT for i in range(1, length)]
speed = 100
is_game_over = False

#---------------------------------------------
def create_fruit(color_frame):
    while True:   
        rcol = random.randint(0, width - 1)
        rrow = random.randint(0, height - 1)
        if color_frame[rrow][rcol] == BACKGROUND:
            color_frame[rrow][rcol] = FRUIT
            break

def display(color_frame):  
    canvas.delete()
    for h in range(0, height):
        for w in range(0, width):
            sx = cr * w
            sy = cr * h
            ex = sx + cr - 1
            ey = sy + cr - 1
            color = color_frame[h][w]
            if color == BACKGROUND:
                fill = 'black'
            elif color == SNAKE:
                fill = 'red'
            else:
                fill = 'green'
            canvas.create_rectangle(sx, sy, ex, ey, outline='black', fill=fill)

# Creating List
def init_game(color_frame):
    for h in range(0, height):
        row = []
        for w in range(0, width):
            r = BACKGROUND
            row.append(r)
        color_frame.append(row)
    for i in range(0, length):
        color_frame[0][i] = SNAKE
    for i in range(0, 3):
        create_fruit(color_frame)


def run_game_loop():
    move(color_frame)
    display(color_frame)
    if not is_game_over: 
        root.after(speed, run_game_loop)

def game_over():
    global is_game_over
    for i in range (0, height):
            for j in range(0, width):
                color_frame[i][j] = SNAKE
    is_game_over = True



def move(color_frame):
    global head, tail, length
    ate_fruit = False
    x, y = head
    if direct == RIGHT:
        x += 1
    elif direct == LEFT:
        x -= 1
    elif direct == DOWN:
        y += 1
    else:
        y -= 1
    x = x % width
    y = y % height

    if color_frame[y][x] == SNAKE:
        game_over()
        
    if color_frame[y][x] == FRUIT:
        ate_fruit = True
        length += 1

    head = (x, y)
    stack.append(direct)
    color_frame[y][x] = SNAKE
    if ate_fruit == True:
        create_fruit(color_frame)
        return
    
    x, y = tail
    color_frame[y][x] = BACKGROUND
    tail_direct = stack.pop(0)
    if tail_direct == RIGHT:
        x += 1
    elif tail_direct == LEFT:
        x -= 1
    elif tail_direct == DOWN:
        y += 1
    else:
        y -= 1
    x = x % width
    y = y % height
    tail = (x, y)

def change_direct(event):
    global direct
    if event.keysym == 'Right' and direct != LEFT:
        direct = RIGHT
    elif event.keysym == 'Left' and direct != RIGHT:
        direct = LEFT
    elif event.keysym == 'Down' and direct != UP:
        direct = DOWN
    elif event.keysym == 'Up' and direct != DOWN:
        direct = UP


#---------------------------------------------------------

init_game(color_frame)
root = tk.Tk()
root.title("Snake Game Chinu ")
canvas = tk.Canvas(root, width=width * cr, height=height * cr)
canvas.pack()
root.bind('<Right>', change_direct)
root.bind('<Left>', change_direct)
root.bind('<Up>', change_direct)
root.bind('<Down>', change_direct)
run_game_loop()



# Run the Tkinter main loop
root.mainloop()
