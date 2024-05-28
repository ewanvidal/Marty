from martypy import Marty
from sensors import *

def avance(my_marty,distance):
    my_marty.stand_straight()
    for i in range(distance):
        obstacleL = my_marty.foot_obstacle_sensed('left')
        obstacleR = my_marty.foot_obstacle_sensed('right')
        groundSensorL = my_marty.get_ground_sensor_reading('left')
        groundSensorR = my_marty.get_ground_sensor_reading('right')
        if (groundSensorL>30 and groundSensorR>30 and not(obstacleL) and not(obstacleR)):
            my_marty.walk(1,'auto',0,25,1500,None)
def rotate(my_marty,angle):
    my_marty.stand_straight()
    if(angle>0):
        while(angle>15):
            my_marty.walk(0,'auto',15)
            angle=angle-15
            print(angle)
        my_marty.walk(0,'auto',angle)
    else :
        while(angle<-15):
            my_marty.walk(0,'auto',-15)
            angle=angle+15
        my_marty.walk(0,'auto',angle)
def retourner(my_marty):
    rotate(my_marty,180)
def recule(my_marty,distance):
    my_marty.walk(distance,'auto',0,-25,1500,None)

def deplacement_couleur(couleur):
    if (couleur in ["green","yellow","blue","red","purple"]):
        if (couleur=="green"):
            return "forward"
        if (couleur=="blue"):
            return "left"
        if (couleur=="purple"):
            return "right"
        if (couleur=="yellow"):
            return "backwards"
        if (couleur=="red"):
            return "center"
    else :
        print("Couleur non valide")

def movementColorLab(my_marty):
    color = getColorReading(my_marty)
    movement = deplacement_couleur(color)
    if movement == "forward" :
        avance(my_marty,3)
        return False
    elif movement == "left" :
        my_marty.sidestep('left', 3)
        return False
    elif movement == "right" :
        my_marty.sidestep('right', 3)
        return False
    elif movement == "backwards" :
        retourner(my_marty)
        avance(my_marty,3)
        return False
    else :
        return True














        