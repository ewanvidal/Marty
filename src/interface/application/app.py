from martypy import Marty
import time
from connexion import connexion
from deplacement import avance,rotate,recule
def main():
    
    (connecter,my_marty)=connexion(True)
    if(connecter):print("le robot est connecté")
    avance(my_marty,10)
main()
