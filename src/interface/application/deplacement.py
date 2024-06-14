#----------------------------------------------------------
# Projet : Marty
#----------------------------------------------------------
# Historique :
# Version     | Date        | Nom                   | Description
# 1.00.00     |  12/06/2024 | Joachim/Natthan/Ewan  | Version initiale
#----------------------------------------------------------

# ----------------------------------------------------------
# Fonction : Avance
# Description : Utilise la fonction de référence walk afin de faire
# marcher le robot d'un certain nombre de pas passé en paramètre
# ----------------------------------------------------------

def avance(my_marty,distance):
    for i in range(distance):
        my_marty.walk(1,'auto',0,25, 1500, None)

# ----------------------------------------------------------
# Fonction : Rotate
# Description : Marty effectue une rotation d'un certain angle
# passé en paramètre
# ----------------------------------------------------------
 
def rotate(my_marty,angle):
   
    if(angle>0):
        while(angle>15):
            my_marty.walk(0,'auto',15)
            angle=angle-15
            print(angle)
        my_marty.walk(0,'auto',angle)
    else :
        while(angle<-15):
            my_marty.walk(0,'auto',-15)
            angle=angle+15
        my_marty.walk(0,'auto',angle)
    
# ----------------------------------------------------------
# Fonction : Retourner
# Description : Marty se retourne de 180° afin de marcher
# ----------------------------------------------------------

def retourner(my_marty):
   rotate(my_marty,180)

# ----------------------------------------------------------
# Fonction : Recule
# Description : Marty recule grâce à la fonction de référence walk
# ----------------------------------------------------------

def recule(my_marty,distance):
    my_marty.walk(distance,'auto',0,-25, 1500, None)

# ----------------------------------------------------------
# Fonction : deplacement_couleur
# Description : Récupère une couleur et associe le mouvement
# correspondant
# ----------------------------------------------------------

def deplacement_couleur(couleur):
    if (couleur in ["green","yellow","blue","red","pink", "lightblue", "black"]):
        if (couleur=="green"):
            return "forward"
        if (couleur=="blue"):
            return "right"
        if (couleur=="pink"):
            return "left"
        if (couleur=="yellow"):
            return "backwards"
        if (couleur=="red"):
            return "center"
        if (couleur=="lightblue"):
            return "forward"
        if (couleur=="black"):
            return "action"
    else :
        print(couleur)
        print("Couleur non valide")

# ----------------------------------------------------------
# Fonction : movementDirection
# Description : Associe un mouvement à l'appel d'une fonction 
# créée dans ce fichier, forward appelle avance par exemple
# ----------------------------------------------------------

def movementDirection(my_marty,movement):
    if movement == "forward" :
        avance(my_marty,6)
        return False
    elif movement == "left" :
        my_marty.sidestep('left', 6)
        return False
    elif movement == "right" :
        my_marty.sidestep('right', 6)
        return False
    elif movement == "backwards" :
        recule(my_marty,6)
        return False
    else :
        return True





        