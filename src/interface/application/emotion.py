from martypy import Marty
def regard(my_marty,pose_or_angle='normal'):
    if (type(pose_or_angle)==int):
        my_marty.eyes(pose_or_angle)
    elif(pose_or_angle in ['angry','excited','normal','wide','wiggle']):
        my_marty.eyes(pose_or_angle)
    else: 
        print("Marty n'accepte que le format entier et les mots angry, excited, normal, wide, et wiggle pour ses yeux")

def danse(my_marty,direction='right',type_dance=1, temps=3000):
    if (type_dance==1):
        my_marty.dance(direction,temps)
    else :
        my_marty.circle_dance(direction,temps)

def celebre(my_marty,temps=4000):
    my_marty.celebrate(temps)
