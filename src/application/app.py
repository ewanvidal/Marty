from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule
def main():
    
    (connecter,my_marty)=connexion(True)
    if(connecter):print("le robot est connecté")
    avance(5,my_marty)
    recule(5,my_marty)
    rotate(117,'right',my_marty)
main()