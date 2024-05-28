from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule,retourner,deplacement_couleur,movementColorLab
from emotion import regard,danse,celebre
from sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft

def labyrinthe():
    (connecter1,my_marty1)=connexion(True,"192.168.0.9")
    (connecter2,my_marty2)=connexion(True,"192.168.0.10")
    if (connecter1):print("Le robot 1 est connecté")
    if (connecter2):print("Le robot 2 est connecté")
    if (not(connecter1 and connecter2)):
        print("Erreur de connexion, il faut que les deux robots soient connecté")
        return 0
    end1=False
    end2=False
    while (end1==False or end2==False):
        if (end1==False):
            end1=movementColorLab(my_marty1)
        if (end2==False):
            end2=movementColorLab(my_marty2)
    if (end1 and end2):
        celebre(my_marty1)
        celebre(my_marty2)
    



