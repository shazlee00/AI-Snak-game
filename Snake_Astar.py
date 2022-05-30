import imp
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import SearchAgent






screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    #snake.move()
    #Detect collision with food.
    steps=SearchAgent.solve('Astar',snake.head.position(), food.position())
    print("step are:",steps['solution'])
    if(steps):     
        for action in steps['solution']:
            screen.update()
            time.sleep(0.05)
            if action=='up':
                snake.up()
                print(snake.head.position())
                time.sleep(0.08)
            if action=='down':
                snake.down()
                print(snake.head.position())
                time.sleep(0.08)
            if action=='left':
                snake.left()
                print(snake.head.position())
                time.sleep(0.08)
            if action=='right':
                snake.right()       
                print(snake.head.position())
                time.sleep(0.08)
        if snake.head.distance(food) <=20:
            food.refresh()
            #snake.extend()
            scoreboard.increase_score()        
      







