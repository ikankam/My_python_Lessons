from turtle import Turtle

POS_INCREASE = -20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360
pos = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """Creates the snake (3 square segments)"""
        for new_seg in range(0, 3):
            self.add_segment(new_seg)

    def add_segment(self, seg_position):
        """Adds segment to the snake"""
        global pos
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setx(pos)
        new_turtle.pos()
        self.segment.append(new_turtle)
        # print(new_turtle.pos()) debugging purposes
        pos += POS_INCREASE

    def extend(self):
        """Extends the snake"""
        self.add_segment(self.segment[-1].pos())
        # print(self.segment[-1].pos()) debugging purposes

    def move(self):
        """Keeps snake moving across the screen. Creates a uniform motion for turtle segments.
        Segment 2 goes to segment 1 position and segment 1 goes to segment 0's position.
        Segment 0 does the turns."""

        for turtle_seg in range(len(self.segment) - 1, 0, -1):
            new_x_pos = (self.segment[turtle_seg - 1]).xcor()
            new_y_pos = self.segment[turtle_seg - 1].ycor()
            self.segment[turtle_seg].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Resetting snake after collision with wall or tail"""
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    # Setting up keyboard responses to direct snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
