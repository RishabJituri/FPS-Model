from ursina import *
from ursina.shaders import lit_with_shadows_shader
from player import player
# from enemy import enemy


app = Ursina()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
wall1 = Entity(model = 'cube', texture='wall', collider='cube',scale = (200,10,200), position = (0,0,0))
# wall2 = duplicate(wall1,z=-25)
# wall3 = duplicate(wall1,rotation_y=90,x=-25,z=0)
ceiling = Entity(model='plane', collider='box', scale=(200,10,200), texture='grass', texture_scale=(4,4))


editor_camera = EditorCamera(enabled=False, ignore_paused=True)



player = player(ground)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))



gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.clear, on_cooldown=False)
# gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)

shootables_parent = Entity()
mouse.traverse_target = shootables_parent


def update():
    
    if held_keys['left mouse']:
        if player.bullets>0:
            shoot()
            
    # if held_keys['shift'] and crouching == False:
    #     print(player.scale)        
    #     player.scale[1] = 0.5
    #     crouching = True
        
    # if held_keys['shift up'] and crouching == True:
    #     player.scale[1] = 1
        
        

def shoot():
    if not gun.on_cooldown:
        player.bullets-=1
        
        # print('shoot')
        gun.on_cooldown = True
        # gun.muzzle_flash.enabled=True
        from ursina.prefabs.ursfx import ursfx
        # ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
        # invoke(gun.muzzle_flash.disable, delay=.05)
        invoke(setattr, gun, 'on_cooldown', False, delay=.15)
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            mouse.hovered_entity.hp -= 1
            mouse.hovered_entity.blink(color.red)




class Enemy(Entity):
    def __init__(self,**kwargs):
        
        super().__init__(parent=shootables_parent, model='cube', scale_y=2.5, origin_y=-.5, color=color.blue, collider='box', **kwargs)
        # self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 10
        self.hp = self.max_hp
        self.player = player
    # def shoot(self):
        
        
    def update(self):
        dist = distance_xz(self.player.position, self.position)
        if  dist < 2:
            return

        # self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        # print(hit_info.entity)
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 10
            if dist < 5:
                player.health-= 10*time.dt
                print(player.health)
                if player.health <= 0:
                    quit()
                    return -1
                

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            # _enemiesleft = enemies_left - 1
            # if enemies_left <= 0:
            #     quit()
            #     return 1
            
            player.bullets += 10
            return

        # self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        # self.health_bar.alpha = 1
enemies = []

def spawn_enemy():
    enemy = Enemy()
    x = x = random.choice([random.uniform(-100, -10), random.uniform(10, 100)])  # Adjust range based on your map size
    y = 0  # Keep them on the ground level
    z = random.uniform(-100, 100)
    enemy.position = (x,y,z)
    enemies.append(enemy)

# List to keep track of enemies

# Spawn multiple enemies
for _ in range(50):  # Change 5 to however many enemies you want
    spawn_enemy()

enemies_left = len(enemies)




def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)


ambient_light = AmbientLight(color=color.white)
# sun.look_at(Vec3(1,-1,-1))


app.run()