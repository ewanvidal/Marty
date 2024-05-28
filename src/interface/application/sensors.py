from martypy import Marty

def getColorReading(my_marty):
    reading = my_marty.get_ground_sensor_reading("left")
    if reading == 36 or reading == 37:
        return "green"
    elif reading > 114:
        return "yellow"
    elif reading == 39 or reading == 40:
        return "blue"
    elif reading > 97 and reading < 105:
        return "red"
    elif reading > 31 and reading < 34:
        return "purple"
    else :
        print("Demandez aux développeurs d'ajouter cette couleur dans la base de données")

def getColorReadingRGB(my_marty):
    reading_red = my_marty.get_color_sensor_value_by_channel("left", "red")
    reading_blue = my_marty.get_color_sensor_value_by_channel("left", "blue")
    reading_green = my_marty.get_color_sensor_value_by_channel("left", "green")
    if (reading_red > 63 and reading_red < 65.5) and (reading_green > 56 and reading_green < 59) and (reading_blue > 86 and reading_blue < 89) :
        return "blue"
    elif (reading_red > 167 and reading_red < 171) and (reading_green > 25 and reading_green < 27.5) and (reading_blue > 39 and reading_blue < 42) :
        return "red"
    elif (reading_red > 190 and reading_red < 196) and (reading_green > 93 and reading_green < 95) and (reading_blue > 65 and reading_blue < 68) :
        return "yellow"
    elif (reading_red > 60 and reading_red < 62) and (reading_green > 42.5 and reading_green < 44.5) and (reading_blue > 34 and reading_blue < 36) :
        return "green"
    elif (reading_red > 53 and reading_red < 57) and (reading_green > 26 and reading_green < 30) and (reading_blue > 46 and reading_blue < 49) :
        return "purple"
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