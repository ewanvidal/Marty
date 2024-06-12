#from connexion import connexion
from application.deplacement import avance,recule,deplacement_couleur,movementDirection
from application.emotion import regard,danse,celebre
from application.sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft, getColorReadingRGB
from time import *
N=3

def getEnd(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j]=="red":
                return (i,j)
def getStart(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j]=="lightblue":
                return (i,j)
def updatePosition(deplacement,x,y):
    if (deplacement=="green" or deplacement=="lightblue"):
        return(x+1,y)
    elif deplacement=="yellow":
        return(x-1,y)
    elif deplacement=="pink":
        return(x,y-1)
    elif deplacement=="blue":
        return(x,y+1)
                
def getLabyrintheColor(my_marty1,my_marty2):
    #(connecter1,my_marty2)=connexion(True,"192.168.0.101")
    #(connecter2,my_marty2)=connexion(True,"192.168.0.10")
    connecter2=True
    connecter1=True
    if (not(connecter1 and connecter2)):
        print("Erreur de connexion, il faut que les deux robots soient connecté")
        return 0
    tableau = [["none"] * 3 for _ in range(3)]
    color = getColorReadingRGB(my_marty1,1)
    tableau[0][2]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1,1)
    tableau[1][2]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1,1)
    tableau[2][2]=color
    movementDirection(my_marty1,"left")
    color = getColorReadingRGB(my_marty1,1)
    tableau[2][1]=color
    movementDirection(my_marty1,"backwards")
    color = getColorReadingRGB(my_marty1,1)
    tableau[1][1]=color
    movementDirection(my_marty1,"backwards")
    color = getColorReadingRGB(my_marty1,1)
    tableau[0][1]=color
    movementDirection(my_marty1,"left")
    color = getColorReadingRGB(my_marty1,1)
    tableau[0][0]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1,1)
    tableau[1][0]=color
    movementDirection(my_marty1,"forward")
    color = getColorReadingRGB(my_marty1,1)
    tableau[2][0]=color
    for i in range(3):
        print(tableau[i])
    print("Est ce que le deuxième robot est prêt à partir ?")
    go= input()
    if (go!="non"):
        color = getColorReadingRGB(my_marty2,2)
        if tableau[0][2]=="black" and color!="black":
            tableau[0][2]=color
        movementDirection(my_marty2,"forward")
        color = getColorReadingRGB(my_marty2,2)        
        if tableau[1][2]=="black" and color!="black":
            tableau[1][2]=color
        movementDirection(my_marty2,"forward")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[2][2]=="black" and color!="black":
            tableau[2][2]=color
        movementDirection(my_marty2,"left")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[2][1]=="black" and color!="black":
            tableau[2][1]=color
        movementDirection(my_marty2,"backwards")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[1][1]=="black" and color!="black":
            tableau[1][1]=color
        movementDirection(my_marty2,"backwards")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[0][1]=="black" and color!="black":
            tableau[0][1]=color
        movementDirection(my_marty2,"left")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[0][0]=="black" and color!="black":
            tableau[0][0]=color
        movementDirection(my_marty2,"forward")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[1][0]=="black" and color!="black":
            tableau[1][0]=color
        movementDirection(my_marty2,"forward")
        color = getColorReadingRGB(my_marty2,2)
        if tableau[2][0]=="black" and color!="black":
            tableau[2][0]=color
        for i in range(3):
            print(tableau[i])
    return tableau

def executeLabyrinthe(my_marty,tableau):
    print("Est ce que le robot est sur la case de départ ?")
    go= input()
    if go=="non":return 0
    debut=getStart(tableau)
    fin =getEnd(tableau)
    x,y=debut
    while ((x,y)!=fin):
            color=tableau[x][y]
            print(color,x,y)
            x,y=updatePosition(color,x,y)
            movement = deplacement_couleur(color)
            movementDirection(my_marty,movement)
    my_marty.celebrate()