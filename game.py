import tkinter
import random

#CONSTANTS
WIDTH = 540
HEIGHT = 480
BG_COLOR = 'white'
MAIN_BALL_COLOR = 'blue'
MAIN_BALL_RADIUS = 25
INIT_DX = 1
INIT_DY = 1
DELAY = 8
MAX_RADIUS = 35
MIN_RADIUS = 15
BAD_COLOR = 'red'
COLORS = ['aqua', 'fuchsia', BAD_COLOR, 'pink', 'yellow', BAD_COLOR, 'gold', 'chartreuse', BAD_COLOR]

#CLASSES
class Ball():
    def __init__(self, x, y, r, color, dx = 0, dy = 0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = BG_COLOR, outline = BG_COLOR)

    def move(self):
        # collision with the walls
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


    #mouse events
def mouse_click(event):
    global main_ball
    if event.num == 1:  # left mouse button
        if 'main_ball' not in globals():  # старт
            main_ball = Ball(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            if main_ball.x > WIDTH / 2:
                main_ball.dx = -main_ball.dx
            if main_ball.y > HEIGHT / 2:
                main_ball.dy = -main_ball.dy
            main_ball.draw()
        else: # turn left
            if main_ball.dy * main_ball.dx > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3:  # right mouse button: turn right
        if main_ball.dy * main_ball.dx > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy
   # print(event.num, event.x, event.y)



# create a list of objects-balls
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Ball(random.choice(range(MAX_RADIUS, WIDTH - MAX_RADIUS)),
                         random.choice(range(MAX_RADIUS, HEIGHT - MAX_RADIUS)),
                         random.choice(range(MIN_RADIUS, MAX_RADIUS)),
                         random.choice(COLORS))
        lst.append(next_ball)
        next_ball.draw()
    return lst



def main():
    if "main_ball" in globals():
        main_ball.move()
    root.after(DELAY, main)



#---------------MAIN-------------------------#
root = tkinter.Tk()
root.title("Game_Balls")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()
canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Button-2>", mouse_click, "+")
canvas.bind("<Button-3>", mouse_click, "*")
if "main_ball" in globals():
    del main_ball
main()
balls = create_list_of_balls(1111)
root.mainloop()
