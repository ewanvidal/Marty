from martypy import Marty
def regard(my_marty,pose_or_angle):
    if (type(pose_or_angle)==int):
        my_marty.eyes(pose_or_angle)

