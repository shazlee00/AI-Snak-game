from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")
        

    
    
    def create_snake(self):
         for position in STARTING_POSITIONS:
            self.add_segment(position)
        #self.add_segment(STARTING_POSITIONS[0])


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        

    def up(self):
        self.head.setheading(UP)
        self.move()
        #self.head.forward(MOVE_DISTANCE) 
            

    def down(self):
        self.head.setheading(DOWN)
        self.move()
        #self.head.forward(MOVE_DISTANCE) 
            

    def left(self):
        self.head.setheading(LEFT)
        self.move()
        #self.head.forward(MOVE_DISTANCE)    

    def right(self):
        self.head.setheading(RIGHT)
        #self.head.forward(MOVE_DISTANCE)
        self.move()







    # def up(self):
    #     if self.head.heading() != DOWN:
    #         self.head.setheading(UP)
    #         self.head.forward(MOVE_DISTANCE)
    #         #self.move()
            

    # def down(self):
    #     if self.head.heading() != UP:
    #         self.head.setheading(DOWN)
    #         self.head.forward(MOVE_DISTANCE)
    #         #self.move()
            

    # def left(self):
    #     if self.head.heading() != RIGHT:
    #         self.head.setheading(LEFT)
    #         self.head.forward(MOVE_DISTANCE)
    #         #self.move()
            

    # def right(self):
    #     if self.head.heading() != LEFT:
    #         self.head.setheading(RIGHT)
    #         self.head.forward(MOVE_DISTANCE)
    #         #self.move()
            
