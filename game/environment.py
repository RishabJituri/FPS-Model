from ursina import *

class environment():
    def ___init__(self):
        self.ground = Entity(model='plane', texture= "grass", collider='box', scale=100)
        self.wall1 = Entity(model = 'cube', texture='wall', collider='cube',scale = (50,10,0), position = (0,5,50))
        self.wall2 = duplicate(self.wall1,z=-25)
        self.wall3 = duplicate(self.wall1,rotation_y=90,x=-25,z=0)
        