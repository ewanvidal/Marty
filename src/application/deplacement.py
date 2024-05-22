from martypy import Marty
def avance(distance,my_marty):
    my_marty.stand_straight()
    my_marty.walk(distance,'auto',0,25,1500,None)
def rotate(angle,my_marty):
    if(angle>0):
        while(angle>20):
            my_marty.walk(1,'auto',20)
            angle=angle-20
        my_marty.walk(1,'auto',angle)
    else :
        while(angle<-20):
            my_marty.walk(1,'auto',-20)
            angle=angle+20
        my_marty.walk(1,'auto',angle)
def recule(distance,my_marty):
    rotate(180,my_marty)
    avance(distance,my_marty)