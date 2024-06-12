#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

from martypy import Marty

# ----------------------------------------------------------
# Fonction : 
# Description :
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