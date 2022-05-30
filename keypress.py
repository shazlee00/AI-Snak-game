from pynput.keyboard import Key,Controller
import time
import random
time.sleep(5)
stroke=Controller()
def play():
    while(True):
        moves=['up','down','left','irght']
        move=random.choice(moves)
        time.sleep(0.5)

        stroke.press('right')
        stroke.release('right')
        time.sleep(0.5)
        stroke.press('up')
        stroke.release('up')
        time.sleep(0.5)
        stroke.press('left')
        stroke.release('left')
        time.sleep(0.5)
        stroke.press('down')
        stroke.release('down')


        # if move=='Up':
        #     stroke.press("Up")
        #     stroke.release("Up")
        # elif move=='Down':
        #     stroke.press("Down")
        #     stroke.release("Down")
        # elif move=='Right':
        #     stroke.press("Right")
        #     stroke.release("Right")
        # elif move=='Left':
        #     stroke.press("Left")
        #     stroke.release("Left")




