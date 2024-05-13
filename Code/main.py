import martypy 
connectionWifi=True
if (connectionWifi):
    my_marty = martypy.Marty("wifi", "192.168.0.5")
else:
    my_marty = martypy.Marty("USB")