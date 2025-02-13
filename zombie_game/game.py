from ursina import *
from ursina.shaders import lit_with_shadows_shader
from player import player

class game(Ursina):
    
    def __init__(self):
        super().__init__()
        self.ground = Entity(model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
        self.player = player(self.ground)
        self.enemies = []
        self.enemies_len = 0
    
    def play(self):
        Entity.default_shader = lit_with_shadows_shader
        editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self.player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
        shootables_parent = Entity()
        mouse.traverse_target = shootables_parent
        self.run()
    
    def update(self):
        if held_keys['left mouse']:
            if self.player.bullets>0:
                self.player.shoot()

        
        
        
        