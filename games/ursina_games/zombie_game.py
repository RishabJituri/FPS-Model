from ursina import *
import ursina.camera as Camera
from panda3d.core import GraphicsOutput, GraphicsBuffer, Texture
from panda3d.core import WindowProperties
from ursina.shaders import lit_with_shadows_shader
from .player import player
from .enemy import Enemy
import pygame



class game():
    def __init__(self):
        
        self.app = Ursina(window_type="offscreen")
        self.clock =pygame.time.Clock()
        self.ground = Entity(
            model='plane', collider='box', scale=200, 
            texture='grass', texture_scale=(4,4)
        )
        self.player = player(self.ground)  
        
        self.enemies = []
        
    def spawn_enemy(self,shootables_parent):
        enemy = Enemy(self.player,shootables_parent)
        x = random.choice(
            [random.uniform(-100, -10), random.uniform(10, 100)]
        )  
        
        y = 0  
        z = random.uniform(-100, 100)
        enemy.position = (x,y,z)
        self.enemies.append(enemy)
        
    def play(self):
        error_level=0
        # self.app.win.set_visible(False)
        Entity.default_shader = lit_with_shadows_shader
        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent
        for _ in range(20):  self.spawn_enemy(shootables_parent)
        ambient_light = AmbientLight(color=color.white)
        # while len(scene.entities) > 27:
            
        #     self.clock.tick(60)
            
        #     self.app.step()
        self.app.run()
        print(1)
        return 1
        
    



        
        