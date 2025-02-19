from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController

class player(FirstPersonController):
    def __init__(self, ground):
        super().__init__()
        self.model='cube'
        self.z=-10
        self.color=color.orange
        self.origin_y=-.5
        self.speed=8
        self.health=100
        self.cursor.model = 'sphere'
        self.cursor.scale = 0.001
        self.cursor.color=color.black
        self.position = ground.position
        self.bullets = 50
        
        self.gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.clear, on_cooldown=False)
    
    def shoot(self):
        
        if not self.gun.on_cooldown:
            self.bullets-=1
            self.gun.on_cooldown = True
            invoke(setattr, self.gun, 'on_cooldown', False, delay=.15)
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp') and distance_xz(self.position,mouse.hovered_entity.position) < 20:
                mouse.hovered_entity.hp -= 1
                mouse.hovered_entity.blink(color.red)
    
    def update(self):
        super().update()
        if held_keys['left mouse']:
            if self.bullets>0:
                self.shoot()
    
        
    