from ursina import *
from ursina.shaders import lit_with_shadows_shader
from player import player
from enemy import Enemy

class game():
    
    def __init__(self):
        # self.app = Ursina(headless=True)
        
        self.ground = Entity(
            model='plane', collider='box', scale=200, 
            texture='grass', texture_scale=(4,4)
        )
        self.player = player(self.ground)  
        self.enemies = []
        self.enemies_len = 0
    
    def spawn_enemy(self,shootables_parent):
        enemy = Enemy(self.player,shootables_parent)
        x = x = random.choice(
            [random.uniform(-100, -10), random.uniform(10, 100)]
        )  
        y = 0  
        z = random.uniform(-100, 100)
        enemy.position = (x,y,z)
        self.enemies.append(enemy)
        
    def play(self):
        def update():
            if held_keys['left mouse']:
                if self.player.bullets>0:
                    self.player.shoot()
        
        Entity.default_shader = lit_with_shadows_shader
        editor_camera = EditorCamera(enabled=False, 
                                     ignore_paused=True
                                     )

        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent
        for _ in range(50):  # Change 5 to however many enemies you want
            self.spawn_enemy(shootables_parent)
        self.enemies_len = len(self.enemies)
        
        ambient_light = AmbientLight(color=color.white)
        self.app.run()
    
    

g = game()

        
        