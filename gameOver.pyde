gameOver = True
class player:
    def __init__(self):
        self.j_flag = False
        self.grav_flag = True
        self.eyeY = 1.5
        self.ptY = 1.5
        self.fov = PI/3
        self.speed = 40
        self.flag = 1
        self.score = 0
        self.highscore = 0
        
    def jump(self):
        self.eyeY += 0.1
        self.ptY +=0.05
        
    def grav(self):
        self.eyeY -= 0.1
        self.ptY -= 0.05
    
    def reset(self):
        self.j_flag = False
        self.grav_flag = True
        
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
    global obs, base_ht, pl
    size(600, 600, P3D)
    base_ht = height-100
    obs = []
    pl = player()
    z_val = -500*10
    for i in range(6):
        o = obstacle(z_val, random(100, 150))
        obs.append(o)
        z_val -= 850

def draw():
    global pl, obs, base_ht, gameOver
    if gameOver == False:
        background(137, 207, 240)
        frameRate(int(pl.speed))
        
        cameraZ = (height/2.0) / tan(pl.fov/2.0)
        perspective(pl.fov, float(width/2)/float(height/2), 50, -cameraZ*20)
    
        if pl.j_flag == True:
            pl.jump()
        
        if pl.eyeY >= 4 and pl.ptY >= 3:
            pl.reset()
    
        if pl.grav_flag == True:
            if pl.eyeY > 1.5 and pl.ptY > 1.5:
                pl.grav()
            else:
                pl.flag = 1
        
        camera(width/2, height/pl.eyeY, 60, width/2, height/pl.ptY, -100, 0, 1, 0)
        
        lights()
        
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
            
            if ob.z >= 55:
                if ((height/pl.eyeY) - (base_ht-ob.ht)) > 0:
                    gameOver = True
            
    else:
        background(0)
        perspective()
        camera()
        textSize(32);
        textAlign(CENTER)
        fill(200);
        text("GAME OVER", width/2-2, height/2-2)
        fill(255) 
        text("GAME OVER", width/2, height/2)
        textSize(14)
        text("Press Space To Replay", width/2, 550)


        
def keyPressed():
    global pl, gameOver, obs
    if key == CODED:
        if keyCode == UP and pl.flag == 1:
            pl.j_flag = True
            pl.grav_flag = False
            pl.flag += 1
    if key == ' ':
        gameOver = False
        pl.score = 0
        pl.speed = 40
        z_val = -500*10
        for ob in obs:
            ob.z = z_val
            z_val -= 850
