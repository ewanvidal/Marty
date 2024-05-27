from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule,retourner
from emotion import regard,danse,celebre

def labyrinthe():
    (connecter1,my_marty1)=connexion(True,"192.168.0.9")
