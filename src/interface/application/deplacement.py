from martypy import Marty
def avance(my_marty,distance):
    my_marty.stand_straight()
    my_marty.walk(distance,'auto',0,25,1500,None)
def rotate(my_marty,angle):
    my_marty.stand_straight()
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
def retourner(my_marty,distance):
    rotate(my_marty,180)
    avance(my_marty,distance)
def recule(my_marty,distance):
    my_marty.walk(distance,'auto',0,-25,1500,None)