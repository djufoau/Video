from ursina import *

app = Ursina()

#platform package

from ursina.prefabs.platformer_controller_2d import PlatformerController2d

#player
player = PlatformerController2d(y=1, z=.01, scale_y=0.5, max_jumps=1)

#ground

ground3 = Entity(model='cube', color=hsv(100,90,50), scale=(10,0.5,1),position=(16,6,0) ,collider='box')
ground2 = Entity(model='cube', color=hsv(100,90,50), scale=(20,0.5,1),collider='box')
ground = Entity(model='cube', color=hsv(100,90,50), scale=(10,0.5,1),position=(12,3,0) ,collider='box')

#camera
camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 32

#Audio

a = Audio('sine', loop=False, autoplay=True)

a.volume = .5

def input(key):
    if key == 'space':
        a = Audio('sine', pitch=random.uniform(.5,1), loop=False)


#EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()

