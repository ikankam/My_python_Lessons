import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.level_boost = 0

    def create_new_car(self):
        """Create a new car of random color beginning from right end of screen"""
        random_select = random.choice(COLORS)
        # print (random_select)
        if random_select == "red":
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(320, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        """Moves cars along x-axis towards the left"""
        for car in self.car_list:
            x_change = car.xcor() - (STARTING_MOVE_DISTANCE+self.level_boost)
            car.goto(x_change, car.ycor())

    def level_up(self):
        """Increases level by 10"""
        self.level_boost += MOVE_INCREMENT
