from martypy import Marty
def avance(distance,my_marty):
    my_marty.walk(distance,'auto',0,25,1500,None)

def connexion(connexionWifi=True, ip_adress="192.168.0.100"):
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
        

(connecter,my_marty)=connexion(True,"192.168.0.100")
if(connecter):print("le robot est connecter")
avance(5,my_marty)