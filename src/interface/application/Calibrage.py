#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

import os

premiereFois = True
dicoCouleur = {}

# ----------------------------------------------------------
# Fonction : getCouleurCalibrage(color,numero)
# Description : Lis dans un fichier nommé Calibrage<numero>.txt les valeurs de la couleur passé en argument et enregistre dans un dictionnaire pour que l'appel soit plus rapide 
# ----------------------------------------------------------

def getCouleurCalibrage(color,numero):
    name="Calibrage"+str(numero)+".txt"
    global premiereFois
    if premiereFois:
        dossier = os.path.dirname(__file__)
        chemin_fichier = os.path.join(dossier, name)
        with open(chemin_fichier, "r", encoding='utf-8') as fichier:
            for ligne in fichier:
                ligneSplit = ligne.split()
                if len(ligneSplit) == 4:
                    dicoCouleur[ligneSplit[0]] = (float(ligneSplit[1]), float(ligneSplit[2]), float(ligneSplit[3]))
        premiereFois = False

    if color in dicoCouleur:
        return dicoCouleur[color]
    else:
        print("Couleur non valide")

# ----------------------------------------------------------
# Fonction : Calibrage(my_marty, color, numero)
# Description : enregiste dans un fichier nommé Calibrage<numero>.txt les valeurs de la couleur passé en argument
# ----------------------------------------------------------

def Calibrage(my_marty, color, numero):
    name="Calibrage"+str(numero)+".txt"
    dossier = os.path.dirname(__file__)
    chemin_fichier = os.path.join(dossier, name)
    
    with open(chemin_fichier, "r", encoding='utf-8') as fichierLecture:
        lignes = fichierLecture.readlines()

    position = -1
    for i, ligne in enumerate(lignes):
        if ligne.startswith(color):
            position = i
            break

    reading_red = my_marty.get_color_sensor_value_by_channel("left", "red")
    reading_green = my_marty.get_color_sensor_value_by_channel("left", "green")
    reading_blue = my_marty.get_color_sensor_value_by_channel("left", "blue")

    if position != -1:
        lignes[position] = f"{color} {reading_red} {reading_green} {reading_blue}\n"
    else:
        lignes.append(f"{color} {reading_red} {reading_green} {reading_blue}\n")

    with open(chemin_fichier, "w", encoding='utf-8') as fichier:
        fichier.writelines(lignes)

    with open(chemin_fichier, "r", encoding='utf-8') as fichier:
        print(fichier.read())


