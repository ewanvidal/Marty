#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

#from connexion import connexion
from application.deplacement import avance,recule,deplacement_couleur,movementDirection
from application.emotion import regard,danse,celebre
from application.sensors import getColorReading,getObstacleLeft,getObstacleRight,getGroundRight,getGroundLeft,getDistRight,getDistLeft, getColorReadingRGB
from time import *
N=3

# ----------------------------------------------------------
# Fonction : getEnd(tableau)
# Description : renvoie la position de la couleur rouge représentant la fin 
# ----------------------------------------------------------

def getEnd(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j]=="red":
                return (i,j)

# ----------------------------------------------------------
# Fonction : getStart(tableau)
# Description : renvoie la position de la couleur bleu clair représentant le début 
# ----------------------------------------------------------

def getStart(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j]=="lightblue":
                return (i,j)

# ----------------------------------------------------------
# Fonction : updatePosition(deplacement,x,y)
# Description : renvoie la prochaine position en fonction de la couleur en suivant le schéma suivant:
#                   green ↑     yellow ↓    pink ←      blue→ 
# ----------------------------------------------------------

def updatePosition(deplacement,x,y):
    if (deplacement=="green" or deplacement=="lightblue"):
        return(x+1,y)
    elif deplacement=="yellow":
        return(x-1,y)
    elif deplacement=="pink":
        return(x,y-1)
    elif deplacement=="blue":
        return(x,y+1)

# ----------------------------------------------------------
# Fonction : correction tableau
# Description : corrige l'erreur qui faisait que le tableau était affiché en mirroir
# ----------------------------------------------------------

def correction(tableau):
    for i in range(len(tableau)):
        varInt=tableau[i][0]
        tableau[i][0]=tableau[i][2]
        tableau[i][2]=varInt
    return tableau

# ----------------------------------------------------------
# Fonction : getLabyrintheColor(my_marty1,my_marty2)
# Description : effectue la reconnaissance pour détecter les couleurs puis les stocker dans un tableau
#               Le chemin suivi est le suivant: ↑↑←↓↓←↑↑←
#               Avant que le deuxième robot parte, il faut écrire quelque chose d'autre que non dans la console
#               Renvoie un tableau contenant les couleurs recconnues 
# ----------------------------------------------------------

def getLabyrintheColor(my_marty1,my_marty2):
    #(connecter1,my_marty2)=connexion(True,"192.168.0.101")
    #(connecter2,my_marty2)=connexion(True,"192.168.0.10")
    #connecter2=True
    #connecter1=True
    #if (not(connecter1 and connecter2)):
        #print("Erreur de connexion, il faut que les deux robots soient connecté")
        #return 0

    
    tableau = [["none"] * 3 for _ in range(3)]  #crée le tableau
    color = getColorReadingRGB(my_marty1,1)     #récupère la couleur au sol 
    tableau[0][2]=color                         #actualise le tableau
    movementDirection(my_marty1,"forward")      #fais avancer marty
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
        if tableau[0][2]=="black" and color!="black":   #vérifie que la couleur n'est pas noir et que la couleur précédemment enregistrés peut être remplacée 
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

# ----------------------------------------------------------
# Fonction :    executeLabyrinthe(my_marty,tableau):
# Description : effectue le chemin passé en argument via le tableau calculé dans la fonction précédente
# ----------------------------------------------------------

def executeLabyrinthe(my_marty,tableau):
    print("Est ce que le robot est sur la case de départ ?")
    go= input()
    if go=="non":return 0
    debut=getStart(tableau)
    fin =getEnd(tableau)
    x,y=debut
    while ((x,y)!=fin):                         # Tant qu'on est pas à la fin, on lit la couleur dans le tableau et effectue la tache associé 
            color=tableau[x][y]
            print(color,x,y)
            x,y=updatePosition(color,x,y)
            movement = deplacement_couleur(color)
            movementDirection(my_marty,movement)
    my_marty.celebrate()