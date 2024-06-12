from martypy import Marty
def connexion(connexionWifi=True, ip_adress="192.168.0.103"):
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