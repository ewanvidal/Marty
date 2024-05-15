import martypy
def connexion(connexionWifi=True, ip_adress="192.168.0.100"):
    if connexionWifi:
        try:
            my_marty = martypy.Marty("wifi", ip_adress)
            return True
        except: 
            print("connexion wifi impossible")
            return False
    else:
        try:
            my_marty = martypy.Marty("USB")
            return True
        except: 
            print("connexion USB impossible")
            return False