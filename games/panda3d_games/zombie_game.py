from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
import sys

class FPSGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Disable mouse default control
        self.disableMouse()
        
        # Set up first-person camera
        self.camLens.setFov(90)
        self.camera.setPos(0, 0, 2)
        
        # Load environment
        self.environment = loader.loadModel("models/environment")
        self.environment.reparentTo(render)
        self.environment.setScale(0.25, 0.25, 0.25)
        self.environment.setPos(-8, 42, 0)
        
        # Load player collision
        self.collisionSetup()
        
        # Keyboard controls
        self.keyMap = {"forward": False, "backward": False, "left": False, "right": False}
        self.accept("escape", sys.exit)
        self.accept("w", self.setKey, ["forward", True])
        self.accept("w-up", self.setKey, ["forward", False])
        self.accept("s", self.setKey, ["backward", True])
        self.accept("s-up", self.setKey, ["backward", False])
        self.accept("a", self.setKey, ["left", True])
        self.accept("a-up", self.setKey, ["left", False])
        self.accept("d", self.setKey, ["right", True])
        self.accept("d-up", self.setKey, ["right", False])
        
        # Mouse look
        self.taskMgr.add(self.mouseTask, "mouseTask")
        
        # Movement task
        self.taskMgr.add(self.update, "updateTask")
    
    def setKey(self, key, value):
        self.keyMap[key] = value
    
    def update(self, task):
        dt = globalClock.getDt()
        moveSpeed = 10 * dt
        if self.keyMap["forward"]:
            self.camera.setY(self.camera, moveSpeed)
        if self.keyMap["backward"]:
            self.camera.setY(self.camera, -moveSpeed)
        if self.keyMap["left"]:
            self.camera.setX(self.camera, -moveSpeed)
        if self.keyMap["right"]:
            self.camera.setX(self.camera, moveSpeed)
        return Task.cont
    
    def mouseTask(self, task):
        if base.mouseWatcherNode.hasMouse():
            md = base.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            centerX = base.win.getXSize() // 2
            centerY = base.win.getYSize() // 2
            
            # Rotate camera
            self.camera.setH(self.camera.getH() - (x - centerX) * 0.1)
            self.camera.setP(self.camera.getP() - (y - centerY) * 0.1)
            
            base.win.movePointer(0, centerX, centerY)
        return Task.cont
    
    def collisionSetup(self):
        # Player collision sphere
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        
        self.playerCollider = CollisionNode("player")
        self.playerCollider.addSolid(CollisionSphere(0, 0, 1, 1))
        self.playerColliderNP = self.camera.attachNewNode(self.playerCollider)
        self.cTrav.addCollider(self.playerColliderNP, self.pusher)
        self.pusher.addCollider(self.playerColliderNP, self.camera, base.drive)

if __name__ == "__main__":
    game = FPSGame()
    game.run()
