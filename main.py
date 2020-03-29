#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import random
import threading
import time


# Write your program here
#Initialize
touchR = TouchSensor(Port.S4)
touchL = TouchSensor(Port.S1)
motorL = Motor(Port.B)
motorR = Motor(Port.C)
powl = [0, 500, -500, 500, 0  , -250 , -500, 500, 250 ]
powr = [0, 500, -500, 0  , 500, -500, -250 , 250 , 800]
brick.light(Color.BLACK)
i = random.randint(0, 8)
T_set = 10



#write module
def Sound():
    while True:
        brick.sound.beep()
        brick.light(Color.RED)
        wait(100)
        brick.light(Color.GREEN)
        

def MotorOn():
    global powl
    global powr
    global i
    global MIN
    global MAX
    while True:
        motorL.run(powl[i])
        motorR.run(powr[i])
        wait(1000)
        i = random.randint(0, 8)
        #create randint


while not Button.CENTER in brick.buttons():
    brick.display.text("Set Seconds Timer", (20, 20))
    brick.display.text(str(T_set) + "s", (60, 50))
    wait(100)
    if Button.DOWN in brick.buttons():
        while Button.DOWN in brick.buttons():
            pass
        T_set-=1
        if T_set <= 1:
            T_set = 1
    elif Button.UP in brick.buttons():
        while Button.UP in brick.buttons():
            pass
        T_set+=1
    brick.display.clear()

thread_1 = threading.Thread(target = MotorOn)
thread_2 = threading.Thread(target = Sound)
offset = time.time()
cnt = T_set
while cnt >= 0:
    #print(cnt)
    #wait(100)
    now = time.time() - offset
    cnt = round(T_set - now)
    brick.display.text(str(cnt)+" Sec", (50, 65))
    wait(100)
    brick.display.clear()


thread_1.start()
thread_2.start()
brick.display.image('Hurt.bmp')
while True:
    if touchR.pressed() and Button.CENTER in brick.buttons():
        break

    if touchL.pressed():
        brick.sound.file('dog_bark_2.wav', volume=100)
        wait(3000)
        brick.sound.Stop()


motorL.run(0)
motorR.run(0)
brick.display.image('Up.bmp')
wait(1000)
