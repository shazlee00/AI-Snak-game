import imp
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import SearchAgent
from block import Block





screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
blocks=[]
postions = [
                [200,200],
                [-123,-134],
                [150,-50],
                [-100,200],
                [-169,24],
                [-123,145],
                [-69,69]             
 ]
for i in postions:
    blocks.append(Block(i))


scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    #snake.move()
    #Detect collision with food.
    steps=SearchAgent.solve('Astar',snake.head.position(), food.position(),blocks)
    for i in steps: print(i,steps[i])
    if(steps):     
        for action in steps['solution']:
            screen.update()
            time.sleep(0.05)
            if action=='up':
                snake.up()
                time.sleep(0.08)
            if action=='down':
                snake.down()
                time.sleep(0.08)
            if action=='left':
                snake.left()
                time.sleep(0.08)
            if action=='right':
                snake.right()       
                time.sleep(0.08)
        if snake.head.distance(food) <=20:
            food.refresh()
            for block in blocks:
                if block.distance(food) <= block.r:
                    food.refresh()        
            #snake.extend()
            scoreboard.increase_score()        
      







