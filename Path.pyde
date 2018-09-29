
def setup():
    global base_ht
    size(600, 600,  P3D)
    base_ht = height-100

def draw():
    global base_ht
    background(137, 207, 240)
    fov = PI/3
    cameraZ = (height/2.0) / tan(fov/2.0)
    perspective(fov, float(width/2)/float(height/2), 50, -cameraZ*20)

    pushMatrix()
    translate(width/2, base_ht, 0)
    strokeWeight(1)
    fill(0)
    stroke(0)
    box(width/1.5, height/6, 500*100)
    popMatrix()
