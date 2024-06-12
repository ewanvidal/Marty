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
    tableau = [["none"] * 3 for _ in range(3)]
    color = getColorReadingRGB(my_marty1)
    tableau[0][2]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1)
    tableau[1][2]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1)
    tableau[2][2]=color
    movementDirection(my_marty1,"left")
    color = getColorReadingRGB(my_marty1)
    tableau[2][1]=color
    movementDirection(my_marty1,"backwards")
    color = getColorReadingRGB(my_marty1)
    tableau[1][1]=color
    movementDirection(my_marty1,"backwards")
    color = getColorReadingRGB(my_marty1)
    tableau[0][1]=color
    movementDirection(my_marty1,"left")
    color = getColorReadingRGB(my_marty1)
    tableau[0][0]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1)
    tableau[1][0]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1)
    tableau[2][0]=color
    for i in range(3):
        print(tableau[i])
    print("Est ce que le deuxième robot est prêt à partir ?")
    go= input()
    if (go!="non"):
        color = getColorReadingRGB(my_marty1)
        if tableau[0][2]=="black":
            tableau[0][2]=color
        movementDirection(my_marty1,"forward")
        color = getColorReadingRGB(my_marty1)        
        if tableau[1][2]=="black":
            tableau[1][2]=color
        movementDirection(my_marty1,"forward")
        color = getColorReadingRGB(my_marty1)
        if tableau[2][2]=="black":
            tableau[2][2]=color
        movementDirection(my_marty1,"left")
        color = getColorReadingRGB(my_marty1)
        if tableau[2][1]=="black":
            tableau[2][1]=color
        movementDirection(my_marty1,"backwards")
        color = getColorReadingRGB(my_marty1)
        if tableau[1][1]=="black":
            tableau[1][1]=color
        movementDirection(my_marty1,"backwards")
        color = getColorReadingRGB(my_marty1)
        if tableau[0][1]=="black":
            tableau[0][1]=color
        movementDirection(my_marty1,"left")
        color = getColorReadingRGB(my_marty1)
        if tableau[0][0]=="black":
            tableau[0][0]=color
        movementDirection(my_marty1,"forward")
        color = getColorReadingRGB(my_marty1)
        if tableau[1][0]=="black":
            tableau[1][0]=color
        movementDirection(my_marty1,"forward")
        color = getColorReadingRGB(my_marty1)
        if tableau[2][0]=="black":
            tableau[2][0]=color
        for i in range(3):
            print(tableau[i])
    return tableau

"""
    x=0
    y=N-1
    for i in range(N):
        for j in range(N):
            print(x,y)
            color = getColorReadingRGB(my_marty1)
            if (color!=None):
                if (y==1):
                    x=x-1
                    position1.updatePositionByValues((x,y),color)
                    error=movementDirection(my_marty1,"backwards")
                    print(error)
                else :
                    x=x+1
                    position1.updatePositionByValues((x,y),color)
                    error=movementDirection(my_marty1,"forward")
                    print(error)

            else :
                sleep(2)
        j=j-1
        color = getColorReadingRGB(my_marty1)
        position1.updatePositionByValues((i,j),color)
        error=movementDirection(my_marty1,"left")
        
    print(position1.getTableau())
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
                        error=movementDirection(my_marty1,"backwards")
                    else :
                        x=x+1
                        position2.updatePositionByValues((x,y),color)
                        error=movementDirection(my_marty1,"forward")
                else :
                    sleep(N-1)
            j=j-1
            color = getColorReadingRGB(my_marty1)
            position1.updatePositionByValues((i,j),color)
            error=movementDirection(my_marty1,"left")
        print(position2.getTableau())
    """
        
        

