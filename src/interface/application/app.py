from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule
def main():
    
    (connecter,my_marty)=connexion(True)
    if(connecter):print("le robot est connecté")
    avance(my_marty,5)
    recule(my_marty,2)
    #rotate(180,my_marty)
main()