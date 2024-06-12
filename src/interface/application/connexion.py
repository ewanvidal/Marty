#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

from martypy import Marty

# ----------------------------------------------------------
# Fonction : Connexion
# Description : Essaye d connecter Marty via USB et prends
# en paramètres l'adresse IP puis essaye de se connecter avec 
# celle-ci
# ----------------------------------------------------------

def connexion(connexionWifi=True, ip_adress="192.168.116.149"):
    if connexionWifi:
        try:
            my_marty = Marty("wifi", ip_adress)
            return (True,my_marty)
        except: 
            print("connexion wifi impossible")
            return (False,None)
    else:
        try:
            my_marty = Marty("USB")
            return (True,my_marty)
        except: 
            print("connexion USB impossible")
            return (False,None)