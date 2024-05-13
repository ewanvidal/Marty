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

#distance en mm (retourne un entier)
#my_marty.get_distance_sensor() 
#Niveau de batterie de marty : 
#my_marty.get_power_status()
#Obstacle devant marty
#Replace 'RightIRFoot' with your IR or color sensors name.
#Your IR sensor can be named either 'LeftIRFoot' or 'RightIRFoot'
#Your color sensor can be named either 'LeftColorSensor' or 'RightColorSensor'
#my_marty.foot_obstacle_sensed('RightIRFoot')
#
