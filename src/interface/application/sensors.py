from martypy import Marty

def getColorReading(my_marty):
    reading = my_marty.get_ground_sensor_reading("left")
    color = str(reading)
    if color == "36" or color == "37":
        color = "green"
        return color
    elif reading >114:
        color = "yellow"
        return color
    elif color == "39" or color == "40":
        color = "blue"
        return color
    elif reading > 97 or reading < 105:
        color = "red"
        return color
    elif color == "31" or color == "32" or color=="33" or color=="34":
        color = "purple"
        return color
    else :
        print("Demandez aux développeurs d'ajouter cette couleur dans la base de données")

def getObstacleLeft(my_marty):
    obstacleL = my_marty.foot_obstacle_sensed('LeftColorSensor')
    return obstacleL

def getObstacleRight(my_marty):
    obstacleR = my_marty.foot_obstacle_sensed('right')
    return obstacleR

def getGroundRight(my_marty):
    onGroundR = my_marty.foot_on_ground('right')
    return onGroundR

def getGroundLeft(my_marty):
    onGroundL = my_marty.foot_on_ground('left')
    return onGroundL

def getDistRight(my_marty) :
    distR = my_marty.get_obstacle_sensor_reading('right')
    return distR

def getDistLeft(my_marty) :
    distL = my_marty.get_obstacle_sensor_reading('left')
    return distL