from ursina import *
from ursina.shaders import lit_with_shadows_shader
from player import player
from enemy import Enemy
import pygame

class game():
    
    def __init__(self):
        # window.borderless = False
        # window.position = (-5000, -5000)
        window.show = False
        
        self.app = Ursina(headless=True)
        self.clock =pygame.time.Clock()
        
        
        self.ground = Entity(
            model='plane', collider='box', scale=200, 
            texture='grass', texture_scale=(4,4)
        )
        self.player = player(self.ground)  
        self.enemies = []
        self.enemies_len = 0
        
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
        # window.show = False
        
        Entity.default_shader = lit_with_shadows_shader
        # editor_camera = EditorCamera(enabled=False, 
        #                              ignore_paused=True
        #                              )
        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent
        for _ in range(10):  # Change 5 to however many enemies you want
            self.spawn_enemy(shootables_parent)
        self.enemies_len = len(self.enemies)
        ambient_light = AmbientLight(color=color.white)
        while True:
            
            # self.clock.tick(1)
            self.app.step()
    
g = game()
g.play()


        
        