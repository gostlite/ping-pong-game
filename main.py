import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


l1_position = -380, 0
r1_position = 380, 0

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


ball = Ball()
score = Score()
l_player = Paddle(l1_position)
r_player = Paddle(r1_position)




game_is_on = True



screen.listen() 
screen.onkey(r_player.up, "Up")
screen.onkey(l_player.up, "w")
screen.onkey(r_player.down, "Down")
screen.onkey(l_player.down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_player) < 50 and ball.xcor() > 340 or ball.distance(l_player) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    if ball.xcor() > 390 :
        score.l_point()
        ball.refresh()



    if  ball.xcor() < -390:
        score.r_point()
        ball.refresh()





screen.exitonclick()
