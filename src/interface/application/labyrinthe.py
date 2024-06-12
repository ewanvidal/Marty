#from connexion import connexion
from application.deplacement import avance,rotate,recule,retourner,deplacement_couleur,movementDirection
from application.emotion import regard,danse,celebre
from application.sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft, getColorReadingRGB
from time import *
from application.position import Position
N=3

def labyrintheColor(my_marty1):
    #(connecter1,my_marty2)=connexion(True,"192.168.0.101")
    #(connecter2,my_marty2)=connexion(True,"192.168.0.10")
    connecter2=True
    connecter1=True
    if (not(connecter1 and connecter2)):
        print("Erreur de connexion, il faut que les deux robots soient connecté")
        return 0
    position1=Position("my_marty1",N)
    x=0
    y=N-1
    for i in range(N):
        for j in range(N):
            color = getColorReadingRGB(my_marty1)
            if (color!=None):
                if (y==1):
                    x=x-1
                    position1.updatePositionByValues((x,y),color)
                    movement = deplacement_couleur("yellow")
                    error=movementDirection(my_marty1,movement)
                else :
                    x=x+1
                    position1.updatePositionByValues((x,y),color)
                    movement = deplacement_couleur("green")
                    error=movementDirection(my_marty1,movement)
            else :
                sleep(2)
        j=j-1
        color = getColorReadingRGB(my_marty1)
        position1.updatePositionByValues((i,j),color)
        movement = deplacement_couleur("yellow")
        error=movementDirection(my_marty1,movement)
    x=0
    y=N-1
    print("Est ce que le deuxième robot est prêt à partir ?")
    go= input()
    if (go!="non"):
        position2=Position("my_marty2",N)
        tableauPos=position1.getTableau()
        for i in range(len(tableauPos)):
            for j in range(len(tableauPos[i])):
                position2.updateTableau(tableauPos[i][j])
        for i in range(N):
            for j in range(N):
                color = getColorReadingRGB(my_marty1)
                if (color!=None):
                    if (y==1):
                        x=x-1
                        position2.updatePositionByValues((x,y),color)
                        movement = deplacement_couleur("yellow")
                        error=movementDirection(my_marty1,movement)
                    else :
                        x=x+1
                        position2.updatePositionByValues((x,y),color)
                        movement = deplacement_couleur("green")
                        error=movementDirection(my_marty1,movement)
                else :
                    sleep(N-1)
            j=j-1
            color = getColorReadingRGB(my_marty1)
            position1.updatePositionByValues((i,j),color)
            movement = deplacement_couleur("yellow")
            error=movementDirection(my_marty1,movement)
        print(position2.getTableau())

        
        

