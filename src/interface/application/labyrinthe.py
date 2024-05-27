from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule,retourner
from emotion import regard,danse,celebre
from sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft

def labyrinthe():
    (connecter1,my_marty1)=connexion(True,"192.168.0.9")
    (connecter2,my_marty2)=connexion(True,"192.168.0.10")
    

