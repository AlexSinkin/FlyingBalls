from tkinter import *
from random import randint


class Ball:
    def __init__(self, x, y, dx, dy, radius):
        self.oval = canvas.create_oval(x-radius, y-radius, x+radius, y+radius)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius

    def move(self):
        if self.x < self.radius:
            self.dx = -self.dx
            self.x = self.radius
        elif self.x > screen_width - self.radius:
            self.dx = -self.dx
            self.x = screen_width - self.radius
        if self.y < self.radius:
            self.dy = -self.dy
            self.y = self.radius
        elif self.y > screen_height - self.radius:
            self.dy = -self.dy
            self.y = screen_height - self.radius
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        canvas.move(self.oval, self.dx, self.dy)


def move_balls():
    for ball in balls_array:
        ball.move()
    return


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    move_balls()
    sleep_dt = max_sleep_time - speed_scale_step * speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


def create_window(size):
    global canvas, speed_scale
    root.geometry(size)

    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=1)

    speed_scale = Scale(root, orient=HORIZONTAL, length=300,
                        from_=0, to=10, tickinterval=1, resolution=1)
    speed_scale.pack()

# Скорость = 1
    speed_scale.set(1)


def create_balls():
    for i in range(5):
        balls_array.append(
            Ball(randint(0, screen_width),
                 randint(0, screen_height),
                 randint(5, 15),
                 randint(5, 15),
                 40))


root = Tk()
canvas = None
speed_scale = None
freeze = False

create_window("1000x600")
screen_width = 1000
screen_height = 600
max_sleep_time = 1100
speed_scale_step = 100

balls_array = []
create_balls()

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()
