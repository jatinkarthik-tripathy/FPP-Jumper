class obstacle:
    def __init__(self, z, ht):
        self.z = z
        self.ht = ht
    
    def move(self):
        self.z += 10
    
    def check_bounds(self):
        if self.z > 100:
            self.z = -500*10
            self.ht = random(100, 150)

def setup():
    global obs, base_ht
    size(600, 600, P3D)
    base_ht = height-100
    obs = []
    z_val = -500*10
    for i in range(6):
        o = obstacle(z_val, random(100, 150))
        obs.append(o)
        z_val -= 850

def draw():
    global base_ht, obs
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
    
    for ob in obs:
        pushMatrix()
        translate(width/2, base_ht-ob.ht, ob.z)
        fill(255)
        box(200, ob.ht, 50)
        popMatrix()
        ob.move()
        ob.check_bounds()
