import tkinter

#CONSTANTS
WIDTH = 540
HEIGHT = 480
BG_COLOR = 'white'

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
    if event.num == 1:
        main_ball = Ball(event.x, event.y, 30, 'red',1,1)
        main_ball.draw()
        main_ball.move()
    else:
        main_ball.hide()
   # print(event.num, event.x, event.y)

def main():
    if "main_ball" in globals():
        main_ball.move()
    root.after(10, main)



#---------------MAIN-------------------------#
root = tkinter.Tk()
root.title("Game_Balls")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()
canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Button-2>", mouse_click, "+")
canvas.bind("<Button-3>", mouse_click, "*")
main()
root.mainloop()
