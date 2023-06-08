import tkinter as tk
import random

WIDTH,HEIGHT = 500,500

canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()
direction = ''

class Snake:
    def __init__(self):
        self.head = [0,0]
        self.body = []
        self.size = 50
    def update(self, direction,food):
        last = tuple(self.head)

        match direction:
            case "up":
                self.head[1] -= self.size
            case "down":
                self.head[1] += self.size
            case "left":
                self.head[0] -= self.size
            case "right":
                self.head[0] += self.size

        if self.head[0] == WIDTH:
            self.head[0] = 0
        if self.head[0]+self.size <= 0:
            self.head[0] = WIDTH
        if self.head[1] == HEIGHT:
            self.head[1] = 0
        if self.head[1]+self.size <= 0:
            self.head[1] = HEIGHT

        for bod in range(len(self.body)):
            s = self.body[bod]
            self.body[bod] = last
            last = s
        for bod in self.body:
            if bod == tuple(self.head):
                print("game over")
                exit()
        if self.head == food.getPosition():
            self.body.append(tuple(food.getPosition()))
            food.generatePosition()
        
    def draw(self):
        canvas.create_rectangle(self.head[0], self.head[1],self.head[0]+self.size, self.head[1]+self.size, fill='green')
        for i in self.body:
            canvas.create_rectangle(i[0], i[1], i[0]+self.size, i[1]+self.size, fill='red')
class Food:
    def __init__(self):
        self.pos = []
        self.size = 50
    def generatePosition(self):
        x = round(random.randint(0,WIDTH-self.size)/self.size, 0)*self.size
        y = round(random.randint(0,HEIGHT-self.size)/self.size, 0)*self.size
        self.pos = [x,y]
    def draw(self):
        canvas.create_rectangle(self.pos[0], self.pos[1],self.pos[0]+self.size, self.pos[1]+self.size, fill='orange')
    def getPosition(self):
        return self.pos

snake = Snake()
food = Food()


food.generatePosition()
def loop():
    global direction
    canvas.delete('all')
    snake.update(direction,food)
    snake.draw()
    
    food.draw()
    canvas.after(120,loop)
    

def move(event):
    global direction
    match event.char:
        case 'w':
            if direction == 'down':
                return
            direction = 'up'
        case 'a':
            if direction == 'right':
                return
            direction = 'left'
        case 's':
            if direction == 'up':
                return
            direction = 'down'
        case 'd':
            if direction == 'left':
                return
            direction = 'right'

canvas.bind_all('w', move)
canvas.bind_all('a', move)
canvas.bind_all('s', move)
canvas.bind_all('d', move)

loop()

canvas.mainloop()
