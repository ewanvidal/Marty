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
    end2=True
    position1=Position("my_marty1",3)
    while (end1==False or end2==False):
        if (end1==False):
            color = getColorReadingRGB(my_marty1)
            if (color!=None):
                print(position1.getCurrentPosition())
                position1.updatePosition(color)
                movement = deplacement_couleur(color)
                end1=movementDirection(my_marty1,movement)
            else :
                sleep(2)
        #if (end2==False):
            #color = getColorReading(my_marty2)
            #movement = deplacement_couleur(color)
            #end2=movementDirection(my_marty2,movement)
    if (end1 and end2):
        print(position1.getTableau())
        celebre(my_marty1)
        #celebre(my_marty2)

#def labyrintheMur(my_marty1):
    #(connecter1,my_marty2)=connexion(True,"192.168.0.101")
    #(connecter2,my_marty2)=connexion(True,"192.168.0.10")
#    connecter2=True
 #   connecter1=True
  #  if (not(connecter1 and connecter2)):
