from turtle import Turtle

UP = 90

DOWN = 270

RIGHT = 0

LEFT = 180

x = 0

y = 0


MOVE_DISTANCE = 20  # snakes steps

POSITION = [(x, y), (x - 20, y),

            (x - 40, y)]  # set the coordinates  of snake body cell


class Snake(Turtle):

    def __init__(self):

        super().__init__()

        self.snake_body = []  # list of a snake body

        self.create_snake()

        self.snake_head = self.snake_body[0]

    def create_snake(self):

        for cell in POSITION:

            self.add_snake(cell)

    def add_snake(self, position):

        snake_cell = Turtle("circle")  # shape the snake

        snake_cell.penup()

        snake_cell.color("white")  # sate the snake colour

        snake_cell.goto(position)  # set snake cell coordinates

        self.snake_body.append(snake_cell)

    def extend(self):

        self.add_snake(self.snake_body[-1].position())

    def move(self):
        """moving the snake forward"""

        for cell in range(len(self.snake_body) - 1, 0, -1):

            new_coordinate_x = self.snake_body[cell - 1].xcor()

            new_coordinate_y = self.snake_body[cell - 1].ycor()

            self.snake_body[cell].goto(new_coordinate_x, new_coordinate_y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        """ for going to up """

        if self.snake_head.heading() == DOWN:

            pass

        else:

            self.snake_head.setheading(UP)

    def down(self):
        """for going to down """

        if self.snake_head.heading() != UP:

            self.snake_head.setheading(DOWN)

    def right(self):
        """ for going to right """

        if self.snake_head.heading() != LEFT:

            self.snake_head.setheading(RIGHT)

    def left(self):
        """ for going to left """

        if self.snake_head.heading() != RIGHT:

            self.snake_head.setheading(LEFT)
