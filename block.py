from turtle import Turtle
import random

from scipy import rand


class Block(Turtle):

    def __init__(self,postion):
        super().__init__()
        self.shape("circle")
        self.penup()
        strch=random.randrange(1,4,1)
        self.shapesize(stretch_len=strch, stretch_wid=strch)
        self.color("blue")
        self.speed("fastest")
        self.r=20*strch
        self.postion = postion
        self.createBlocks()
    
    def createBlocks(self):        
      
     
        self.goto(self.postion[0], self.postion[1])
 
        # print(pos)
    
