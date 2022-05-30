from math import sqrt
import copy
from turtle import Turtle, right
from snake import Snake
from food import Food
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def ecdis(p1,p2):
    #print("****distance*****")
    #print(p1,p2)
    distance =sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    #print(distance)
    return distance


def get_actions(snake,blocks):
    print("****snake head*****")
    print(blocks[0].position())
    print(blocks[0].r)
    snake_state=list(snake)
    #print('snake_state',snake_state)
    actions=['up','down','left','right']
    for action in actions:
       state=get_state(action,snake_state)
       print('snake state',state)
       for block in blocks:
           print(block.position(),block.r,state,ecdis(state,block.position()),action)
           if ecdis(state,block.position()) <= 0.9*block.r:
               actions.remove(action)
               print('array state',actions)
    
   
    if snake[0] >= 280 and 'right' in actions :
        actions.remove('right')
    if snake[1] >=  280 and 'up' in actions :
        actions.remove('up')    
    if snake[0] <=  -280 and 'left' in actions :
        actions.remove('left')
    if snake[1] <=  -280 and 'down' in actions :
        actions.remove('down')
    print(actions)    
    return actions

def get_state(action,old_head):
    #print("this is get_state old snake pos: ",old_head,id(old_head)) 
    new_snakehead=list(old_head)
    #print("this is get_state snake pos: ",new_snakehead,id(new_snakehead)) 
    print(action)
    if action=='up':
       new_snakehead[1]=new_snakehead[1]+20
       #print("this is get_state old snake pos: ",old_head,id(old_head)) 
       #print("this is get_state snake pos: ",new_snakehead,id(new_snakehead)) 
    if action=='down':
        new_snakehead[1]=new_snakehead[1]-20
        #print("this is get_state old snake pos: ",old_head,id(old_head)) 
        #print("this is get_state snake pos: ",new_snakehead,id(new_snakehead)) 
    if action=='right':
        new_snakehead[0]=new_snakehead[0]+20
        #print("this is get_state old snake pos: ",old_head,id(old_head)) 
        #print("this is get_state snake pos: ",new_snakehead,id(new_snakehead))   
    if action=='left':
        new_snakehead[0]=new_snakehead[0]-20 
        #print("this is get_state old snake pos: ",old_head,id(old_head)) 
        #print("this is get_state snake pos: ",new_snakehead,id(new_snakehead))            
    return tuple(new_snakehead)

def isgoal(snake,food):
   #print("**distance from the food: ",snake.head.distance(food)) 
   if ecdis(snake,food)<20:
        return True

def compute_cost(action,snake,food):
    # snake_copy=copy.copy(snake)
    # next_state=get_state(action,snake_copy.head) 
    
    # if(next_state.head.distance(food)>snake.head.distance(food)):
    #     return 30
    # elif (snake.head.distance(food) == next_state.head.distance(food)):
    #     return 20
    # elif (next_state.head.distance(food) <snake.head.distance(food)):
    #     return 10
    return 1
    
	


def compute_heuristic(snake,food):
    
    #print('compute_heuristic:   ',ecdis(snake,food) )
    return ecdis(snake,food)  