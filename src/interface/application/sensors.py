#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

from martypy import Marty
from application.Calibrage import *

# ----------------------------------------------------------
# Fonction : getColorReading
# Description : 1ère version de l'obtention des valeurs données 
# par le capteur de couleur, renvoie la couleur en str
# ----------------------------------------------------------

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

# ----------------------------------------------------------
# Fonction : getColorReadingRGB
# Description : Permet de comparer la valeur RGB obtenue avec 
# les valeurs qui se situent dans les fichiers de callibrage 1 ou 2 selon le robot
# ----------------------------------------------------------

def getColorReadingRGB(my_marty,numero):
    reading_red = my_marty.get_color_sensor_value_by_channel("left", "red")
    reading_blue = my_marty.get_color_sensor_value_by_channel("left", "blue")
    reading_green = my_marty.get_color_sensor_value_by_channel("left", "green")
    blue_tab = getCouleurCalibrage("blue",numero)
    red_tab = getCouleurCalibrage("red",numero)
    yellow_tab = getCouleurCalibrage("yellow",numero)
    green_tab = getCouleurCalibrage("green",numero)
    pink_tab = getCouleurCalibrage("pink",numero)
    lightblue_tab = getCouleurCalibrage("lightblue",numero)
    black_tab = getCouleurCalibrage("black",numero)
    if (reading_red > (blue_tab[0] - 10) and reading_red < (blue_tab[0] + 10)) and (reading_green > (blue_tab[1] - 10) and reading_green < (blue_tab[1] + 10)) and (reading_blue > (blue_tab[2] - 10) and reading_blue < (blue_tab[2] + 10)) :
        print("blue")
        return "blue"
    elif (reading_red > (red_tab[0] - 10) and reading_red < (red_tab[0] + 10)) and (reading_green > (red_tab[1] - 10) and reading_green < (red_tab[1] + 10)) and (reading_blue > (red_tab[2] - 10) and reading_blue < (red_tab[2] + 10)) :
        print("red")
        return "red"
    elif (reading_red > (yellow_tab[0] - 20) and reading_red < (yellow_tab[0]+ 20)) and (reading_green > (yellow_tab[1] - 20) and reading_green < (yellow_tab[1] + 20)) and (reading_blue > (yellow_tab[2] - 20) and reading_blue < (yellow_tab[2] + 20)) :
        print("yellow")
        return "yellow"
    elif (reading_red > (green_tab[0] - 10) and reading_red < (green_tab[0]+ 10)) and (reading_green > (green_tab[1] - 10) and reading_green < (green_tab[1] + 10)) and (reading_blue > (green_tab[2] - 10) and reading_blue < (green_tab[2] + 10)) :
        print("green")
        return "green"
    elif (reading_red > (pink_tab[0] - 10) and reading_red < (pink_tab[0]+ 10)) and (reading_green > (pink_tab[1] - 10) and reading_green < (pink_tab[1] + 10)) and (reading_blue > (pink_tab[2] - 10) and reading_blue < (pink_tab[2] + 10)) :
        print("pink")
        return "pink"
    elif (reading_red > (lightblue_tab[0] - 10) and reading_red < (lightblue_tab[0]+ 10)) and (reading_green > (lightblue_tab[1] - 10) and reading_green < (lightblue_tab[1] + 10)) and (reading_blue > (lightblue_tab[2] - 10) and reading_blue < (lightblue_tab[2] + 10)) :
        print("lightblue")
        return "lightblue"
    elif (reading_red > (black_tab[0] - 10) and reading_red < (black_tab[0]+ 10)) and (reading_green > (black_tab[1] - 10) and reading_green < (black_tab[1] + 10)) and (reading_blue > (black_tab[2] - 10) and reading_blue < (black_tab[2] + 10)) :
        print("black")
        return "black"
    else :
        print(reading_red,reading_green,reading_blue)
        print("Demandez aux développeurs d'ajouter cette couleur dans la base de données")
        return "yellow"
    
# ----------------------------------------------------------
# Fonction : getObstacleLeft
# Description : Renvoie le fait que le robot détecte un obstacle à gauche
# ----------------------------------------------------------

def getObstacleLeft(my_marty):
    obstacleL = my_marty.foot_obstacle_sensed('LeftColorSensor')
    return obstacleL


# ----------------------------------------------------------
# Fonction : getObstacleRight
# Description : Renvoie le fait que le robot détecte un obstacle à droite
# ----------------------------------------------------------

def getObstacleRight(my_marty):
    obstacleR = my_marty.foot_obstacle_sensed('right')
    return obstacleR

# ----------------------------------------------------------
# Fonction : getGroundRight 
# Description : Renvoie la vaeur donnée par le capteur de sol à droite 
# ----------------------------------------------------------

def getGroundRight(my_marty):
    onGroundR = my_marty.foot_on_ground('right')
    return onGroundR

# ----------------------------------------------------------
# Fonction : getGroundLeft
# Description : Renvoie la vaeur donnée par le capteur de sol à gauche 
# ----------------------------------------------------------

def getGroundLeft(my_marty):
    onGroundL = my_marty.foot_on_ground('left')
    return onGroundL

# ----------------------------------------------------------
# Fonction : getDistRight
# Description : Renvoie la distance mesurée par le capteur à droite
# ----------------------------------------------------------

def getDistRight(my_marty) :
    distR = my_marty.get_obstacle_sensor_reading('right')
    return distR

# ----------------------------------------------------------
# Fonction : getDistLeft
# Description : Renvoie la distance mesurée par le capteur à gauche
# ----------------------------------------------------------

def getDistLeft(my_marty) :
    distL = my_marty.get_obstacle_sensor_reading('left')
    return distL