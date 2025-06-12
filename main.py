
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()  # create a screen object
screen.setup(width=600, height=600)  # set the screen size
screen.title("SNAKE GAME")  # set screen title
screen.bgcolor("black")  # set screen background colour

food = Food()  # Create a food object
screen.tracer(0)  # Turn off the screen
screen.listen()  # Set the screen for listen
snake = Snake()  # Create a snake
scoreboard = Scoreboard()  # Create a score board object
screen.onkey(fun=snake.up, key="Up")  # Key set for going up
screen.onkey(fun=snake.down, key="Down")  # key set for going down
screen.onkey(fun=snake.right, key="Right")  # key set for going right
screen.onkey(fun=snake.left, key="Left")  # key set for going left
game_is_on = True

while game_is_on:
    snake.move()
    # Detect collision with wall
    if (snake.snake_head.xcor() < -280 or snake.snake_head.xcor() > 280) or \
            (snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase()

    # Detect collision with tell
    for cell in snake.snake_body[1:]:
        if snake.snake_head.distance(cell) < 10:
            game_is_on = False
            scoreboard.game_over()

    time.sleep(.1)
    screen.update()
screen.exitonclick()
