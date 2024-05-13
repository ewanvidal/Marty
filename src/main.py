import martypy
def connection(connectionWifi=True, ip_adress="192.168.0.100"):
    if connectionWifi:
        my_marty = martypy.Marty("wifi", ip_adress)
    else:
        my_marty = martypy.Marty("USB")
