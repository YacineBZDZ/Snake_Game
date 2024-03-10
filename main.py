import time
import turtle as t
import snake as s
import Food as f
import scoreboard as sc

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = s.Snake()
food = f.Food()
scoreboard = sc.ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoreincrease()
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or  snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        scoreboard.gameover()

    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameover()
    screen.listen()
    screen.onkey(snake.Up, "Up")
    screen.onkey(snake.Down, "Down")
    screen.onkey(snake.Left, "Left")
    screen.onkey(snake.Right, "Right")


screen.exitonclick()