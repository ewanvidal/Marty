#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

from martypy import Marty
from connexion import connexion
from deplacement import avance,rotate,recule

# ----------------------------------------------------------
# Fonction : Main
# Description :
# ----------------------------------------------------------

def main(): #Teste la fonction connexion et avance de marty 
    
    (connecter,my_marty)=connexion(True)
    if(connecter):print("le robot est connecté")
    avance(my_marty,10) 

main()
