import martypy
def connection(connectionWifi=True, ip_adress="192.168.0.100"):
    if connectionWifi:
        try:
            my_marty = martypy.Marty("wifi", ip_adress)
            return True
        except: 
            print("connection wifi impossible")
            return False
    else:
        try:
            my_marty = martypy.Marty("USB")
            return True
        except: 
            print("connection USB impossible")
            return False
        
