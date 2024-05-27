from martypy import marty

def getColorReading(my_marty):
    reading = my_marty.get_ground_sensor_reading()
    color = str(reading)
    if color == "38" or color == "39":
        color = "green"
        return color
    elif color == "127" or color == "128":
        color = "yellow"
        return color
    elif color == "40" or color == "41":
        color = "blue"
        return color
    elif color == "108" or color == "109":
        color = "red"
        return color
    elif color == "35" or color == "36":
        color == "purple"
        return color
    else :
        print("Demandez aux développeurs d'ajouter cette couleur dans la base de données")

def getObstacleLeft(my_marty):
    obstacleL = my_marty.foot_obstacle_sensed('left')
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