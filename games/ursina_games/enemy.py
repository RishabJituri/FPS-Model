from ursina import *


class Enemy(Entity):
    def __init__(self,player,shootables_parent,**kwargs):
        super().__init__(
            parent=shootables_parent, model='cube', 
            scale_y=2.5, origin_y=-.5, color=color.blue, 
            collider='box', **kwargs
        )
        self.max_hp = 10
        self.hp = self.max_hp
        self.player = player
        self.strike = 0
    
    def update(self):
        dist = distance_xz(self.player.position, self.position) 
        if  dist < 2: return
        self.look_at_2d(self.player.position, 'y')
        hit_info = raycast(
            self.world_position + Vec3(0,1,0), 
            self.forward, 30, ignore=(self,)
            )
        if dist > 2:
            self.position += self.forward * time.dt * 5
        if dist < 5:
            self.player.health-= 10*time.dt
            
            self.strike+=1
            
            if self.player.health <= 0:
                print(-1)
                quit()
                

    @property
    def hp(self):return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            
            self.player.bullets += 10
            return