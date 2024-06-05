import os

premiereFois=True
dicoCouleur={}

def getCouleurCalibrage(color):
    if (premiereFois):
        dossier = os.path.dirname(__file__)
        chemin_fichier = os.path.join(dossier, "Calibrage.txt")
        fichier=open(chemin_fichier,"r")

        for ligne in fichier: 
            ligneSplit=ligne.split()
            dicoCouleur[ligneSplit[0]]=(int(ligneSplit[1]),int(ligneSplit[2]),int(ligneSplit[3]))
    if color in dicoCouleur:
        return dicoCouleur[color]
    else :
        print("Couleur non valide")

def Calibrage(my_marty,color):
    dossier = os.path.dirname(__file__)
    chemin_fichier = os.path.join(dossier, "Calibrage.txt")
    fichierLecture=open(chemin_fichier,"r")
    position=-1
    for i in range(len(fichierLecture)):
        for mot in fichierLecture[i].split():
            if mot==color:
                position=i
    lignes=fichierLecture.readlines()
    reading_red = my_marty.get_color_sensor_value_by_channel("left", "red")
    reading_green = my_marty.get_color_sensor_value_by_channel("left", "green")
    reading_blue = my_marty.get_color_sensor_value_by_channel("left", "blue")
    lignes[position]=(color," ",reading_red," ", reading_green," ",reading_blue,"\n")
    fichier=open(chemin_fichier,"w")
    fichier.writelines(lignes)
    