'''
Draw the house and its image when you perform transformations:
(a) Translation with tx = 2 and ty = 4
(b) Rotation with a = π/3
(c) Scaling with Sx = 2 and Sy = 3
(d) Shear
• along x with Shearx = 0.5
• along y with Sheary = -1.
'''
from pygame import *
def setup():
    size(200, 200)
    background(255)
    noStroke()

    # draw the original position in gray
    fill(192)
    rect(20, 20, 40, 40)
    
    # draw a translucent red rectangle by changing the coordinates
    fill(255, 0, 0, 128)
    rect(20 + 60, 20 + 80, 40, 40)
    
    # draw a translucent blue rectangle by translating the grid
    fill(0, 0, 255, 128)
    pushMatrix()
    translate(60, 80)
    rect(20, 20, 40, 40)
    popMatrix()