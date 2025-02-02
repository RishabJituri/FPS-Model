
from ursina import *
from environment import environment
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

editor_camera = EditorCamera(enabled=True, ignore_paused=True)

player = FirstPersonController(model='cube', z=-10, color=color.orange, origin_y=-.5, speed=8, collider='box')
# player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))


env = environment()

app.run()

