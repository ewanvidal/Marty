#from connexion import connexion
from application.deplacement import avance,rotate,recule,retourner,deplacement_couleur,movementDirection
from application.emotion import regard,danse,celebre
from application.sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft, getColorReadingRGB
from time import *
from application.position import Position

def labyrintheColor(my_marty1):
    #(connecter1,my_marty2)=connexion(True,"192.168.0.101")
    #(connecter2,my_marty2)=connexion(True,"192.168.0.10")
    connecter2=True
    connecter1=True
    if (not(connecter1 and connecter2)):
        print("Erreur de connexion, il faut que les deux robots soient connecté")
        return 0
    end1=False
    end2=False
    position1=Position("my_marty1",3)
    while (end1==False):
            color = getColorReadingRGB(my_marty1)
            if (color!=None):
                print(position1.getCurrentPosition())
                position1.updatePosition(color)
                movement = deplacement_couleur(color)
                end1=movementDirection(my_marty1,movement)
            else :
                sleep(2)
    print("Est ce que le deuxième robot est prêt à partir ?")
    go= input()
    if (go!="non"):
        position2=Position("my_marty2",3)
        tableauPos=position1.getTableau()
        for i in range(len(tableauPos)):
            for j in range(len(tableauPos[i])):
                position2.updateTableau(tableauPos[i][j])
        while (end2==False):
                color = getColorReadingRGB(my_marty1)
                if (color!=None):
                    print(position2.getCurrentPosition())
                    position2.updatePosition(color)
                    movement = deplacement_couleur(color)
                    end1=movementDirection(my_marty1,movement)
                else :
                    sleep(2)
        if (end1 and end2):
            print(position2.getTableau())
            celebre(my_marty1)
            return position2.getTableau()

