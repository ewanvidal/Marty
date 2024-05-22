from martypy import Marty
def avance(distance,my_marty):
    my_marty.stand_straight()
    my_marty.walk(distance,'auto',0,25,1500,None)
def rotate(angle,my_marty):
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
def retourner(distance,my_marty):
    rotate(180,my_marty)
    avance(distance,my_marty)
def recule(distance,my_marty):
    my_marty.walk(distance,'auto',0,-25,1500,None)