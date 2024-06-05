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
            

getCouleurCalibrage("blue")