#Asteroids_beta_ver.2.0

#Fixes:
    #fixed a bug where destroyed by enemyship and enemybullets will not die or lose life
    #fixed an audio distortion issue caused by mission success sound


add_library('minim')

import random

minim = Minim(this)

# run processing in full screenmode
def sketchFullScreen(): 
  return False

#///////////////////////////////////____GLOBAL_VARIABLES///////////////////////////////////
gameover=""
shoot_down =int(0)
numberofasteriods=0
numberofcrashed=0
numberofenemyship = 0
levelscore = 0
defaultnum = 9
bombactive = 0
lifes = []

c=0
d=0
e=0
f=""
g=""

counter = 0
heat = 0
heatsubtract = 0
heatflag = 0
destroyflag = 0

heatnum=0
cooldownflag = 0
thermometer=[]
missionsuccess = ""
login1=""
login2=""
login3=""
scoreboard = ""
bombnumber = ""
lifenum = ""

spaceshipmove = 0
spaceshipleft = 0
spaceshipright = 0
highestspeed = 3.8

scoreboardflag = 0
usernameflag =0
gamecontroller = 0
openningcontroller = 1
instructioncontroller = 0
shipalive_or_dead = 0
thermometerflag = 0
bombflag = 0
enemyshipflag = 0
enemyshipdead = 0

colour = 0
colour2 = 0
circlesize =0 
explosion = 0

n=50
m=180
username= []
p=""

levelnum=""
levels=1
sumlevel = 0

#///////////////////////////////////____CLASSES____//////////////////////////////////////////
class Moveable():
    def move(self):
        self.x = self.x - float(sin(radians(self.direction))*self.speed)
        self.y = self.y + float(cos(radians(self.direction))*self.speed)
        
#///////////////////////////////////////////////////////////////////////////////////////////
class Asteroid(Moveable):
    def __init__(self):
        self.x = random.randint(0,1280)
        self.y = random.randint(0,720)
        self.direction = random.randint(15,350)
        self.speed = random.randint(2,3)
        self.astrsize=random.randint(20,100)
    def draw(self): 
        if self.x > width+self.astrsize:
            self.x = 0-self.astrsize
        if self.x < 0-self.astrsize:
            self.x = width+self.astrsize
        if self.y > height+self.astrsize:
            self.y = 0-self.astrsize
        if self.y < 0-self.astrsize:
            self.y = height+self.astrsize
        fill(0)
        strokeWeight(3)
        ellipse(self.x,self.y,self.astrsize,self.astrsize)
    
#///////////////////////////////////////////////////////////////////////////////////////////        
class Crashedasteroid(Moveable):
    def __init__(self):
        self.x = c
        self.y = d
        self.direction = random.randint(15,350)
        self.speed = random.randint(2,3)
        self.astrsize = e/2
    def draw(self): 
        if self.x > width+self.astrsize:
            self.x = 0-self.astrsize
        if self.x < 0-self.astrsize:
            self.x = width+self.astrsize
        if self.y > height+self.astrsize:
            self.y = 0-self.astrsize
        if self.y < 0-self.astrsize:
            self.y = height+self.astrsize
        fill(0)
        ellipse(self.x,self.y,self.astrsize,self.astrsize)
        
#///////////////////////////////////////////////////////////////////////////////////////////    
class Spaceship():
    def __init__(self):
        self.x = 20000
        self.y = 20000
        self.direction = 180
        self.speed = 0
        self.lives = 3
    def draw(self):
        fill(255)
        strokeWeight(3)
        pushMatrix()
        translate(self.x,self.y) 
        rotate(radians(self.direction))
        triangle(0,25,-13,-8,13,-8)
        strokeWeight(2)
        rect(-2,-12,4,22)
        rect(-15,-17,7,24)
        rect(8,-17,7,24)
        strokeWeight(3)
        triangle(-25,-14,-16,-14,-16,0)
        triangle(25,-14,16,-14,16,0)
        popMatrix()
    def move(self):
        self.x = self.x - int(sin(radians(self.direction))*self.speed*2)
        self.y = self.y + int(cos(radians(self.direction))*self.speed*2)
        if self.x > width:
            self.x = 1
        if self.x < 1:
            self.x = width
        if self.y > height:
            self.y = 1
        if self.y < 1:
            self.y = height
    def turnleft(self):
        self.direction -= 4
    def turnright(self):
        self.direction += 4

#//////////////////////////////////////////////////////////////////////////////////////////        
class Enemyship():
    def __init__(self):
        self.x = random.randint(0,1280)
        self.y = random.randint(0,720)
        self.direction = 0
        self.speed = 2
        self.bullets = []
    def draw(self):
        fill(0)
        strokeWeight(3)
        pushMatrix()
        translate(self.x,self.y) 
        rotate(radians(self.direction))
        triangle(0,25,-13,-8,13,-8)
        popMatrix()
    def move(self):
        self.x = self.x - int(sin(radians(self.direction))*self.speed*2)
        self.y = self.y + int(cos(radians(self.direction))*self.speed*2)
        if self.x > width:
            self.x = 1
        if self.x < 1:
            self.x = width
        if self.y > height:
            self.y = 1
        if self.y < 1:
            self.y = height
    def fire(self):
        enbullets.append(Enbullet())
        
#////////////////////////////////////////////////////////////////////////////////////////////        
class Bullet(Moveable):
    def __init__(self):
        self.x = spaceship.x
        self.y = spaceship.y
        self.direction = spaceship.direction
        self.speed = 8
        self.bulletsize = 5
    def draw(self):
        fill(0,0,0)
        strokeWeight(3)
        ellipse(self.x,self.y,self.bulletsize,self.bulletsize)

#///////////////////////////////////////////////////////////////////////////////////////////
class Enbullet(Moveable):
    def __init__(self):
        self.x = enemyship.x
        self.y = enemyship.y
        self.direction = enemyship.direction
        self.speed = 8
        self.bulletsize = 15
    def draw(self):
        fill(255)
        strokeWeight(4)
        ellipse(self.x,self.y,self.bulletsize,self.bulletsize)
    
#///////////////////////////////////////////////////////////////////////////////////////////   
class Bomb():
    def __init__(self):
        self.bombnum = 4
    def bomb_active(self):
        global numberofcrashed, shoot_down, c, d, e, rocks, scoreboard, bombactive
        for x in range(len(rocks)):
            flag =1
            flag2 = 1
            if self.bombnum >=1:  
                for rock in rocks:
                    if flag2 ==1:
                        if rock.astrsize/2 <= 15 and rock.astrsize/2>0:
                            fill(255)
                            strokeWeight(12)
                            ellipse(c,d,e+11,e+11)
                            rock.astrsize=0  
                            shoot_down += 1
                            scoreboard = "SCORE   "+str(shoot_down) 
                            flag2 = 0
                    if flag == 1:
                        if rock.astrsize/2 > 15:
                            flag = 0
                            e=rock.astrsize
                            rock.astrsize=0   
                            flag2=0
                            c=rock.x
                            d=rock.y
                            shoot_down += 1
                            scoreboard = "SCORE   "+str(shoot_down) 
                            rocks.append(Crashedasteroid())    
                            rocks.append(Crashedasteroid())
                            numberofcrashed +=2
        bombnumber = "Bombs  "+str(self.bombnum)

#///////////////////////////////////////////////////////////////////////////////////////////                        
class Leaderboard():
    def __ini__(self):
        self.players = []
    def draw(self):
        fill(0)
        textSize(70)
        text(f,420,100)
        textSize(40)
        text("Rank",135,160)
        text("Name",390,160)
        text("Score",705,160)
        text("Levels",1000,160)
        textSize(30)
        text("1",170,205)
        text("2",170,250)
        text("3",170,295)
        text("4",170,340)
        text("5",170,385)
        text("6",170,430)
        text("7",170,475)
        text("8",170,520)
        text("9",170,565)
        text("10",170,610)
        if len(self.players)==1:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
        if len(self.players)==2:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250)   
        if len(self.players)==3: 
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
        if len(self.players)==4:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
        if len(self.players)==5:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
        if len(self.players)==6:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
        if len(self.players)==7:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
        if len(self.players)==8:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
        if len(self.players)==9:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
            text(self.players[8][0],390,565)
            text(self.players[8][1],710,565)
            text(self.players[8][2],1040,565)
        if len(self.players)==10:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
            text(self.players[8][0],390,565)
            text(self.players[8][1],710,565)
            text(self.players[8][2],1040,565)
            text(self.players[9][0],390,610)
            text(self.players[9][1],710,610)
            text(self.players[9][2],1040,610)

#///////////////////////////////////////////////////////////////////////////////////////////     
class Player_info():
    def __init__(self):
        self.plist=[]
        self.name = ""
        self.score = 0
        self.level = 0
    def playername(self):
        self.name = p
        self.plist.append(self.name)
    def playerscore(self):
        self.score = shoot_down
        self.plist.append(self.score)
    def playerlevel(self):
        self.level = levels
        self.plist.append(self.level)

#///////////////////////////////////////////////////////////////////////////////////////////
class Username_board():
    def draw(self):
        global m, n
        fill(0)
        textSize(50)
        text("Username:",200,90)
        fill(255)
        strokeWeight(5)
        rect(500,40,550,70)
        strokeWeight(7)
        rect(50,180,1180,472)
        line(168,180,168,652)
        line(286,180,286,652)
        line(404,180,404,652)
        line(522,180,522,652)
        line(640,180,640,652)
        line(758,180,758,652)
        line(876,180,876,652)
        line(994,180,994,652)
        line(1112,180,1112,534)
        line(50,298,1230,298)
        line(50,416,1230,416)
        line(50,534,1230,534)
        fill(0)
        textSize(65)
        text("1",92,259)
        text("2",210,259)
        text("3",328,259)
        text("4",446,259)
        text("5",564,259)
        text("6",682,259)
        text("7",800,259)
        text("8",918,259)
        text("9",1036,259)
        text("0",1154,259)
        text("Q",82,377)
        text("W",200,377)
        text("E",328,377)
        text("R",446,377)
        text("T",564,377)
        text("Y",682,377)
        text("U",795,377)
        text("I",928,377)
        text("O",1030,377)
        text("P",1154,377)
        text("A",89,495)
        text("S",210,495)
        text("D",323,495)
        text("F",446,495)
        text("G",560,495)
        text("H",677,495)
        text("J",810,495)
        text("K",918,495)
        text("L",1036,495)
        text("Z",92,613)
        text("X",210,613)
        text("C",323,613)
        text("V",441,613)
        text("B",564,613)
        text("N",680,613)
        text("M",792,613)
        textSize(70)
        text("/",1147,494)
        textSize(100)
        text("_",900,611)
        textSize(50)
        text("Enter",1050,611)
        if counter%50<=25:
            rect(n+13,m+13,92,92)
            if n==994 and m==534:
                rect(1007,547,210,92)
            if n==1112 and m==534:
                rect(1007,547,210,92)
        if counter%50<=25:
            fill(255)
            textSize(65)
            if n==50 and m==180:
                text("1",92,259)
            if n==168 and m==180:
                text("2",210,259)
            if n==286 and m==180:
                text("3",328,259)
            if n==404 and m==180:
                text("4",446,259)
            if n==522 and m==180:
                text("5",564,259)
            if n==640 and m==180:
                text("6",682,259)
            if n==758 and m==180:
                text("7",800,259)
            if n==876 and m==180:
                text("8",918,259)
            if n==994 and m==180:
                text("9",1036,259)
            if n==1112 and m==180:
                text("0",1154,259)
            if n==50 and m==298:
                text("Q",82,377)
            if n==168 and m==298:
                text("W",200,377)
            if n==286 and m==298:
                text("E",328,377)
            if n==404 and m==298:
                text("R",446,377)
            if n==522 and m==298:
                text("T",564,377)
            if n==640 and m==298:
                text("Y",682,377)
            if n==758 and m==298:
                text("U",795,377)
            if n==876 and m==298:
                text("I",928,377)
            if n==994 and m==298:
                text("O",1030,377)
            if n==1112 and m==298:
                text("P",1154,377)
            if n==50 and m==416:
                text("A",89,495)
            if n==168 and m==416:
                text("S",210,495)
            if n==286 and m==416:
                text("D",323,495)
            if n==404 and m==416:
                text("F",446,495)
            if n==522 and m==416:
                text("G",560,495)
            if n==640 and m==416:
                text("H",677,495)
            if n==758 and m==416:
                text("J",810,495)
            if n==876 and m==416:
                text("K",918,495)
            if n==994 and m==416:
                text("L",1036,495)
            if n==1112 and m==416:
                textSize(70)
                text("/",1147,494)
            if n==50 and m==534:
                text("Z",92,613)
            if n==168 and m==534:
                text("X",210,613)
            if n==286 and m==534:
                text("C",323,613)
            if n==404 and m==534:
                text("V",441,613)
            if n==522 and m==534:
                text("B",564,613)
            if n==640 and m==534:
                text("N",680,613)
            if n==758 and m==534:
                text("M",792,613)
            if n==876 and m==534:
                textSize(100)
                text("_",900,611)
            if n>=994 and m==534:
                textSize(50)
                text("Enter",1050,611)
        textSize(50)
        fill(0)
        text(p,520,90)
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(40)
            text("   Press SHIFT to select         Press SPACE to delete",170,160)
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(40)
            text("   Press SHIFT to select         Press SPACE to delete",170,160)  
           
#//////////////////////////////////////////////////////////////////////////////////////////           
class Instruction():
    def draw(self):
        fill(255)
        strokeWeight(8)
        rect(80,60,1120,600,50)
        fill(0)
        strokeWeight(8)
        line(80,200,1200,200)
        fill(0)
        textSize(85)
        text("Destroy All Asteroids ! ! !",120,160)
        textSize(50)
        text("Press   W   to move forward",120,260)
        text("Press   A   to turn left",120,330)
        text("Press   D   to turn right",120,400)
        text("Press SPACE to Fire ! !",120,470)
        text("Press   S   to hyperspace",120,540)
        text("Press SHIFT to use Bomb",120,610)
        #fill(255)
        #strokeWeight(4)
        #triangle(300,230,315,265,285,265)
        #triangle(280,320,315,307,315,337)
        #triangle(318,385,283,399,283,371)
        #triangle(300,540,315,505,285,505)

        

#///////////////////////////////////CREATING__VARIABLES///////////////////////////////////
rocks=[]
numberofasteriods=defaultnum
for x in range(numberofasteriods):
    rocks.append(Asteroid())
spaceship = Spaceship()
enemyship = Enemyship()
usernameboard = Username_board()
leaderboard = Leaderboard()
instruction = Instruction()
bomb = Bomb()
crashedasteroid = Crashedasteroid()
leaderboard.players = [["jimmy",756990875,524]]


bullets = []
enbullets =[]
login1="Asteroids"
login2="Press SHIFT"

# Arduino globals
# arduinoStoreState = []



#///////////////////////////////////____SETUP____///////////////////////////////////////////
def setup():
    #frameRate(3)
    global bgm, minim,keypress,keydeny,keypress2,yourturn,gate_open,\
    enterthegame,nextlevel,laser,bombsound,explosionsound,asteroidsound,\
    success_sound,arduino,alarm
    
    size(1280,720)
    bgm = minim.loadFile("bgm.mp3")
    keypress = minim.loadFile("keypress.mp3")
    keypress2 = minim.loadFile("keypress2.mp3")
    keydeny = minim.loadFile("keydeny.mp3") 
    yourturn = minim.loadFile("yourturn.mp3")
    gate_open = minim.loadFile("gate_open.mp3")
    enterthegame = minim.loadFile("enterthegame.mp3")
    nextlevel = minim.loadFile("nextlevel.mp3")
    laser = minim.loadFile("laser.wav")
    bombsound = minim.loadFile("ca.aif")
    explosionsound = minim.loadFile("boom.aif")
    asteroidsound = minim.loadFile("150204__killkhan__explosion-1.mp3")
    success_sound = minim.loadFile("unlockcelebration.mp3")
    alarm = minim.loadFile("Woop Woop.mp3")
    bgm.setGain(-15)
    bgm.play()
#     print Arduino.list()
#     arduino = Arduino(this, Arduino.list()[2],57600)
#     for n in range(2,14):
#         arduino.pinMode(n,Arduino.INPUT)
#///////////////////////////////////____DRAW____///////////////////////////////////////////
def draw():
    
    global  gameover, shoot_down ,rocks,numberofasteriods,numberofcrashed,missionsuccess,c \
    ,d,e,levelscore, bullets,login1, login2,scoreboard, login3, levelnum,levels,sumlevel, \
    leaderboard,key,usernameflag , counter,usernameboard, n,m,username,p, gamemode \
    ,gamecontroller, scoreboardflag,openningcontroller, player,shipalive_or_dead, \
    counter,f, colour, colour2, instructioncontroller,defaultnum,bombflag,crashedasteroid \
    ,bombnumber, circlesize,bombactive,heat,heatflag,heatnum,heatsubtract,thermometerflag, \
    thermometer,cooldownflag, g,enemyshipflag,enemyshipdead,numberofenemyship,\
    highestspeed,explosion,lifes,lifenum,destroyflag
    
    background(255)
    print(len(bullets))
#///////////////////////////////////BULLETS__BUGFIXING_PATCH/////////////////////////////////
    if len(bullets)>25:
        bullets.pop(0)
#/////////////////////////////LOCAL_VARIABLES_CHANGE_PER_FRAME//////////////////////////
    if circlesize < 2470 and circlesize > 0 :
        circlesize += 25
    else:
        circlesize = 0
#///////////////////////////////////BOMB_DRAW//////////////////////////////////////////////       
    if bombactive == 1:
        strokeWeight(12)
        fill(255)
        ellipse(spaceship.x,spaceship.y,circlesize,circlesize)       
        strokeWeight(3)
    heat += 1
    counter +=1 
    colour2 +=5
    colour+=5
    if colour == 255:
        colour = 0
    explosion += 1
    
#///////////////////////////////////OPENNING_INTERFACE///////////////////////////////////
    if openningcontroller == 1:
        fill(0)
        textSize(250)
        text(login1,80,370)  #Asteroids
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(45)
            text(login2,500,500)   #Press Enter
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(45)
            text(login2,500,500)   
        
#///////////////////////////////////USERNAME_INTERFACE///////////////////////////////////    
    if usernameflag == 1:
        shipalive_or_dead = 0
        player=Player_info()
        openningcontroller = 0
        #buttonPressed()
        usernameboard.draw()

#///////////////////////////////////INSTRUCTION_INTERFACE///////////////////////////////////
    if instructioncontroller == 1:
        instruction.draw()

#///////////////////////////////////THERMOMETER////////////////////////////////////////////
    if heatflag == 0:
        heatsubtract = heat
    if heatflag == 1:
        heatnum = heat - heatsubtract
    if thermometerflag == 1:
        if heatnum%4 == 1 and heatflag == 1 and cooldownflag == 0:
            thermometer.append("I")
        fill(255)
        strokeWeight(5)
        rect(512,15,370,40)
        fill(0)
        textSize(40)
        text(str("".join(thermometer)),520,50)
        text("HEAT ",400,50)
    if heatflag == 0:
        if counter%12 == 1 and len(thermometer)>0:
            thermometer.pop() 
    if len(thermometer)>30:
        cooldownflag = 1
    if cooldownflag == 1:
        alarm.setGain(10)
        alarm.play()
        highestspeed = 2
        thermometerflag = 0
        fill(255)
        strokeWeight(5)
        rect(512,15,370,40)
        fill(0)
        if colour2%8<=255:
            fill(colour,colour,colour)
            textSize(40)
            text(str("".join(thermometer)),520,50)
            text("OVERHEAT ",295,50)
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(40)
            text(str("".join(thermometer)),520,50)
            text("OVERHEAT ",295,50)
        line(640,18,640,52)
        if len(thermometer)<=10:
            cooldownflag = 0
            thermometerflag = 1
            highestspeed = 3.5
    else:
        alarm.rewind()
            
#///////////////////////////////////SPACESHIP_DRAW/////////////////////////////////////////
    if shipalive_or_dead == 1:
        if counter<=150 and counter%30<=15:
            spaceship.draw()
        elif counter>150:
            spaceship.draw()

#///////////////////////////////////SPACESHIP_MOVE////////////////////////////////////////
    if spaceshipmove==1:
        if shipalive_or_dead == 1:
            pushMatrix()
            translate(spaceship.x,spaceship.y) 
            rotate(radians(spaceship.direction))
            fill(0)
            strokeWeight(3)
            triangle(-11.5,-30,-14,-22,-9,-22)
            triangle(11.5,-30,14,-22,9,-22)
            popMatrix()
        if spaceship.speed <=highestspeed:
            spaceship.speed += 0.12
        if spaceship.speed > highestspeed:
            spaceship.speed = highestspeed
        spaceship.move()
    if spaceshipmove == 0:
        if spaceship.speed >=0:
            spaceship.speed -= 0.08
        if spaceship.speed < 0:
            spaceship.speed  = 0
        spaceship.move()
    if spaceshipleft == 1:
        spaceship.turnleft()
    if spaceshipright == 1:
        spaceship.turnright()
        
    
        
        
#///////////////////////////////////SPACESHIP__HIT__EFFECT///////////////////////////////////
    for rock in rocks:
        if counter >= 150 and shipalive_or_dead == 1:
            if (rock.x - rock.astrsize) < spaceship.x < (rock.x + rock.astrsize) \
            and (rock.y - rock.astrsize) < spaceship.y < (rock.y + rock.astrsize):        
                fill(255)
                strokeWeight(25)
                ellipse(spaceship.x,spaceship.y,180,180)
                shoot_down += 1  
                rock.astrsize=0
                spaceship.lives -= 1
                shipalive_or_dead = 0
                spaceship.x = 20000
                spaceship.y = 20000
                counter = 0
                destroyflag = 1
                explosionsound.setGain(30)
                explosionsound.play()
                explosionsound.rewind()

    fill(0)
    textSize(33)
    text(lifenum,30,150)

            
#///////////////////////////////////BULLETS_DRAW//////////////////////////////////////////
    for bullet in bullets:
        bullet.move()
        bullet.draw()
        if bullet.x > width:
            bullet.bulletsize = 0
        if bullet.x < 0:
            bullet.bulletsize = 0
        if bullet.x > 0 and bullet.x < width and bullet.y < 0:
            bullet.bulletsize = 0        
        if bullet.x > 0 and bullet.x < width and bullet.y >height:
            bullet.bulletsize = 0
            
#///////////////////////////////////ENEMYSHIP__HIT__EFFECT///////////////////////////////////
        if enemyshipflag == 1:
            if (bullet.x - 15) < enemyship.x < (bullet.x + 15) \
            and (bullet.y - 15) < enemyship.y < (bullet.y + 15):    
                enemyshipdead = 1
                explosionsound.setGain(30)
                explosionsound.play()
                explosionsound.rewind()
                fill(255)
                strokeWeight(25)
                ellipse(enemyship.x,enemyship.y,120,120)
                enemyship.x = 12000
                enemyship.y = 12000
                shoot_down += 1
                
#///////////////////////////////////ASTEROIDS__HIT__EFFECT///////////////////////////////////
        for rock in rocks:
            if (rock.x - rock.astrsize) < bullet.x < (rock.x + rock.astrsize) \
            and (rock.y - rock.astrsize) < bullet.y < (rock.y + rock.astrsize):
                asteroidsound.play()
                asteroidsound.rewind()
                c=rock.x
                d=rock.y
                e=rock.astrsize
                rock.astrsize=0
                #rock.x=30000
                #rock.y=10000
                shoot_down += 1
                scoreboard = "SCORE   "+str(shoot_down)
                h = bullet.direction
                bullet.x = 10000
                bullet.y = 10000
                bullet.speed = 0
                bullet.bulletsize = 0
                fill(255)
                strokeWeight(12)
                ellipse(c,d,e+11,e+11)
                if e/2 > 15:
                    rocks.append(Crashedasteroid())
                    rocks.append(Crashedasteroid())
                    numberofcrashed += 2
                #print numberofasteriods,"+", numberofcrashed,"+",numberofenemyship,"=",b-sumlevel
                        
#///////////////////////////////////ENEMY_SHIP//////////////////////////////////////////////// 
    if (levels+1)%3==1:
        for enbullet in enbullets:
            enbullet.move()
            enbullet.draw()
            if enbullet.x > width:
                enbullet.bulletsize = 0
            if enbullet.x < 1:
                enbullet.bulletsize = 0
            if enbullet.x > 1 and enbullet.x < width and enbullet.y < 0:
                enbullet.bulletsize = 0        
            if enbullet.x > 1 and enbullet.x < width and enbullet.y >height:
                enbullet.bulletsize = 0
    if enemyshipflag == 1 and enemyshipdead == 0:
        enemyship.draw()
        enemyship.move()
        if counter%175 == 1:
            enemyship.direction = random.randint(0,359)
        if counter%60 ==1:
            enemyship.fire()    
    
    if (enemyship.x - 8) < spaceship.x < (enemyship.x + 8) \
    and (enemyship.y - 8) < spaceship.y < (enemyship.y + 8):
        enemyshipdead = 1
        explosionsound.setGain(30)
        explosionsound.play()
        explosionsound.rewind()
        fill(255)
        strokeWeight(25)
        ellipse(enemyship.x,enemyship.y,120,120)
        enemyship.x = 12000
        enemyship.y = 12000
        shoot_down += 1
        fill(255)
        strokeWeight(25)
        ellipse(spaceship.x,spaceship.y,180,180)
        spaceship.lives -= 1
        shipalive_or_dead = 0
        spaceship.x = 20000
        spaceship.y = 20000
        counter = 0
        destroyflag = 1
        explosionsound.setGain(30)
        explosionsound.play()
        explosionsound.rewind()
        
#///////////////////////////////////ENEMYBULLET__HIT__EFFECT////////////////////////////////
    for enbullet in enbullets:
        if counter >= 150 and shipalive_or_dead == 1:
            if (enbullet.x - enbullet.bulletsize -4) < spaceship.x < (enbullet.x + enbullet.bulletsize + 4) \
            and (enbullet.y - enbullet.bulletsize - 4) < spaceship.y < (enbullet.y + enbullet.bulletsize +4):
                enbullet.astrsize=0
                enbullet.x = 10000
                enbullet.y = 10000
                fill(255)
                strokeWeight(25)
                ellipse(spaceship.x,spaceship.y,180,180)
                spaceship.lives -= 1
                shipalive_or_dead = 0                
                explosionsound.setGain(15)
                explosionsound.play()
                explosionsound.rewind()
                counter = 0
                destroyflag = 1
                spaceship.x = 20000
                spaceship.y = 20000
    if destroyflag == 1:
        if spaceship.lives >0:
            if counter <= 200:
                fill(0)
                textSize(50)
                text("RESPAWNING...",460,100)
                lifes = []
                for c in range(spaceship.lives):
                    lifes.append("[]")
                lifenum = "LIVES "+"".join(lifes)
            if counter > 200:
                shipalive_or_dead = 1    
                spaceship.x = width/2
                spaceship.y = height/2
                spaceship.direction =180
                destroyflag = 0
                counter = 0
        else:
            counter = 0
            gameover="GAME OVER"
            lifes = []
            lifenum = ""
            player.playerscore()
            player.playerlevel()
            shipalive_or_dead = 0
            spaceship.x = 20000
            spaceship.y = 20000
            gamecontroller = 0
            destroyflag = 0           
#///////////////////////////////////ASTEROIDS_DRAW/////////////////////////////////////////
    for rock in rocks:
        rock.move()
        rock.draw()
        
#///////////////////////////////////TEXT___SCORE___///////////////////////////////////////
    textSize(30)
    text(scoreboard,1070,50)  #score number
    
#///////////////////////////////////TEXT___BOMB_NUMBER___///////////////////////////////////
    textSize(33)
    text(bombnumber,30,100)   

#///////////////////////////////////TEXT___LEVEL_NUMBER___///////////////////////////////////
    textSize(33)
    text(levelnum,30,50)   #level number
         
#////////////////////////////////////TEXT___GAMEOVER___///////////////////////////////////
    fill(0)
    textSize(140)
    text(gameover, 240,390) 
    if counter >150 and gameover == "GAME OVER":
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(40)
            text(" SHIFT  Try again!           SPACE Scoreboard",240,450)
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(40)
            text(" SHIFT  Try again!           SPACE Scoreboard",240,450)
    if scoreboardflag == 1 and counter > 150:
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(40)
            text(" SHIFT  Try again!        SPACE Exit the game",240,700)
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(40)
            text(" SHIFT  Try again!        SPACE Exit the game",240,700)
        
#///////////////////////////////////SCOREBOARD_INTERFACE///////////////////////////////////
    if scoreboardflag == 1:
        lifenum = ""
        thermometerflag= 0
        f = "Leader Board"
        gameover = ""
        scoreboard = ""
        levelnum = ""
        bombnumber = ""
        leaderboard.draw()
    
#///////////////////////////////////GAMERESET__GAMEOVER/////////////////////////////////////


#///////////////////////////////////MISSION__SUCCESS//////////////////////////////////////
    if (levels+1)%3!=1 and gameover != "GAME OVER" and f != "Leader Board":
        if numberofasteriods + numberofcrashed == shoot_down - sumlevel:
            missionsuccess = "Mission Success!"
            fill(0)
            textSize(120)
            text(missionsuccess,160,370) 
            if colour2%510<=255:
                fill(colour,colour,colour)
                textSize(45)
                text("Press SHIFT",480,500)
            if colour2%510>=255:
                fill(255-colour,255-colour,255-colour)
                textSize(45)
                text("Press SHIFT",480,500)
    if (levels+1)%3==1 and gameover != "GAME OVER" and f != "Leader Board":
        if numberofasteriods + numberofcrashed + numberofenemyship == shoot_down - sumlevel:
            missionsuccess = "Mission Success!"
            fill(0)
            textSize(120)
            text(missionsuccess,160,370) 
            if colour2%510<=255:
                fill(colour,colour,colour)
                textSize(45)
                text("Press SHIFT",480,500)
            if colour2%510>=255:
                fill(255-colour,255-colour,255-colour)
                textSize(45)
                text("Press SHIFT",480,500)
    if missionsuccess == "Mission Success!" and gameover != "GAME OVER" and f != "Leader Board":
        success_sound.play()
    else:
        success_sound.rewind()
        success_sound.pause()
        
   
    # call to store arduino button states for next frame  
#     arduinoStoreData()
#     
    
#////////////////////////////////// ARDUINO KEYPRESSED //////////////////////////////////////////
# def arduinoStoreData():
#     """Store data for comparing on next frame and determining if key changed state - ie. LOW to HIGH"""
#     global arduinoStoreState
#     arduinoStoreState = []
#     for n in range(14): # FIXME this number should be a global
#          arduinoStoreState.append(arduino.digitalRead(n))
# 
# 
# 
# def arduinoKeyPressed(pin):
#     """Reads the given pin number and return true for key pressed event - only returns true on first pressed"""
#     if arduino.digitalRead(pin) == Arduino.HIGH and arduinoStoreState[pin] == Arduino.LOW:
#         return True
#     else:
#         return False
#     
# def arduinoKeyReleased(pin):
#     """Reads the given pin number and return true for key released event"""
#     if arduino.digitalRead(pin) == Arduino.LOW and arduinoStoreState[pin] == Arduino.HIGH:
#         return True
#     else:
#         return False
        
    
#///////////////////////////////////____KEYPRESS____////////////////////////////////////////
def keyPressed():
    """ 
    these are the actions when press keys
    """
    global  numberofasteriods, numberofcrashed,bullets, rocks, gameover , missionsuccess,levelscore,\
    shoot_down , login1, login2,scoreboard, login3, levelnum,levels,sumlevel,leaderboard, \
    key,usernameflag,gamemode ,usernameboard, n,m,username,p,gamecontroller, \
    spaceshipright, spaceshipleft, spaceshipmove , scoreboardflag,openningcontroller \
    ,player, shipalive_or_dead,counter,f, instructioncontroller,defaultnum, bombflag, \
    crashedasteroid, bombnumber, circlesize,bombactive,heat,heatflag,heatnum,heatsubtract, \
    thermometerflag,thermometer,cooldownflag,g,enemyshipdead,enemyshipflag,numberofenemyship \
    ,highestspeed,lifenum
    
    
    if openningcontroller == 1:
        if keyCode == SHIFT and counter > 0:
            gate_open.setGain(-3)
            gate_open.play()
            gate_open.rewind()
            usernameflag = 1
            counter = 0
            if usernameflag == 1:
                n =50
                m=180
                username= []
                p=""

    if gameover == "GAME OVER":
        if keyCode == SHIFT and counter>150:
            keydeny.play()
            keydeny.rewind()
            spaceship.lives = 3
            for c in range(spaceship.lives):
                lifes.append("[]")
            lifenum = "LIVES "+"".join(lifes)
            thermometer=[]
            gameover = ""
            player.plist.pop()
            player.plist.pop()
            shoot_down = 0
            numberofcrashed=0
            numberofasteriods = 3
            sumlevel = 0
            levels = 1
            bomb.bombnum = 4
            levelnum = "LEVEL   "+str(levels)
            scoreboard = "SCORE   "+str(shoot_down)
            bombnumber = "Bombs  "+str(bomb.bombnum-1)
            gamecontroller =1
            bullets = []
            rocks=[]
            for x in range(numberofasteriods):
                rocks.append(Asteroid())    
            counter = 0
            spaceship.x= width/2
            spaceship.y =height/2
            spaceship.direction =180
            shipalive_or_dead = 1
            if (levels+1)%3!=1:
                numberofenemyship= 0
                enemyshipflag = 0
                enemyshipdead = 0 
                
        if key == " "and counter>150:
            keypress.play()
            keypress.rewind()
            counter = 0
            leaderboard.players.append(player.plist)
            gamecontroller = 0
            shipalive_or_dead = 0
            spaceship.lives = 3
            scoreboardflag = 1
        

    if missionsuccess == "Mission Success!":
        if keyCode == SHIFT: 
            nextlevel.play()
            nextlevel.rewind()
            thermometer=[]
            counter = 0
            sumlevel = shoot_down
            levels += 1
            levelnum = "LEVEL   "+str(levels)
            missionsuccess = ""
            numberofasteriods += 3
            numberofcrashed = 0
            rocks=[]
            bullets =[]
            for x in range(numberofasteriods):
                rocks.append(Asteroid()) 
            spaceship.x= width/2
            spaceship.y =height/2
            spaceship.direction =180
            shipalive_or_dead =1
            if (levels+1)%3!=1:
                enemyshipflag = 0
                enemyshipdead = 0
            elif (levels+1)%3==1:
                enemyshipflag = 1
                numberofenemyship+=1
            
    
            
            
    if f == "Leader Board":
        if key == " " and counter>0:
            keydeny.play()
            keydeny.rewind()
            f=""
            gameover=""
            gamecontroller = 0
            scoreboardflag = 0
            openningcontroller = 1
            shipalive_or_dead = 0
            spaceship.x = 200000
            spaceship.y = 200000
            enemyshipflag = 0
            shoot_down = 0
            numberofcrashed=0
            sumlevel = 0
            levels = 1
            bomb.bombnum = 4
            rocks=[]
            bullets= []
            numberofasteriods=defaultnum
            for x in range(numberofasteriods):
                rocks.append(Asteroid())
                
        if keyCode == SHIFT and counter>0:
            keypress.play()
            keypress.rewind()
            spaceship.lives = 3 
            for c in range(spaceship.lives):
                lifes.append("[]")
            lifenum = "LIVES "+"".join(lifes)
            counter = 0
            f=""
            gameover=""
            scoreboardflag = 0
            leaderboard.players.pop()
            player.plist.pop() 
            player.plist.pop()
            shoot_down = 0
            spaceship.lives = 3
            enemyshipflag = 0
            numberofcrashed=0
            numberofasteriods = 3
            sumlevel = 0
            levels = 1
            bomb.bombnum = 4
            thermometerflag= 1
            levelnum = "LEVEL   "+str(levels)
            scoreboard = "SCORE   "+str(shoot_down)
            bombnumber = "Bombs  "+str(bomb.bombnum-1)
            gamecontroller =1
            rocks=[]
            bullets =[]
            for x in range(numberofasteriods):
                rocks.append(Asteroid())    
            counter = 0
            spaceship.x= width/2
            spaceship.y =height/2
            spaceship.direction =180
            shipalive_or_dead = 1

            
    if usernameflag == 1 and counter > 0:    
        if keyCode==RIGHT:
            keypress.play()
            keypress.rewind()
            n=n+118
            if n > 1112:
                n =50
        if keyCode==LEFT:
            keypress.play()
            keypress.rewind()
            n=n-118
            if n < 50:
                n = 1112
        if keyCode==UP:
            keypress.play()
            keypress.rewind()
            m=m-118
            if m < 180:
                m = 534
                
                
        if keyCode==DOWN:
            keypress.play()
            keypress.rewind()
            m=m+118
            if m >534:
                m = 180
                
        if key == " ":
            keydeny.play()
            keydeny.rewind()
            if len(username)>0:
                username.pop(len(username)-1)
                p=str("".join(username))
                
        if keyCode == SHIFT and counter>0:
            keypress2.play()
            keypress2.rewind()
            if len(p)<=10:
                if n==50 and m==180:
                    username.append("1")
                    p=str("".join(username))
                if n==168 and m==180:
                    username.append("2")
                    p=str("".join(username))
                if n==286 and m==180:
                    username.append("3")
                    p=str("".join(username))
                if n==404 and m==180:
                    username.append("4")
                    p=str("".join(username))
                if n==522 and m==180:
                    username.append("5")
                    p=str("".join(username))
                if n==640 and m==180:
                    username.append("6")
                    p=str("".join(username))
                if n==758 and m==180:
                    username.append("7")
                    p=str("".join(username))
                if n==876 and m==180:
                    username.append("8")
                    p=str("".join(username))
                if n==994 and m==180:
                    username.append("9")
                    p=str("".join(username))
                if n==1112 and m==180:
                    username.append("0")
                    p=str("".join(username))
                if n==50 and m==298:
                    username.append("Q")
                    p=str("".join(username))
                if n==168 and m==298:
                    username.append("W")
                    p=str("".join(username))
                if n==286 and m==298:
                    username.append("E")
                    p=str("".join(username))
                if n==404 and m==298:
                    username.append("R")
                    p=str("".join(username))
                if n==522 and m==298:
                    username.append("T")
                    p=str("".join(username))
                if n==640 and m==298:
                    username.append("Y")
                    p=str("".join(username))
                if n==758 and m==298:
                    username.append("U")
                    p=str("".join(username))
                if n==876 and m==298:
                    username.append("I")
                    p=str("".join(username))
                if n==994 and m==298:
                    username.append("O")
                    p=str("".join(username))
                if n==1112 and m==298:
                    username.append("P")
                    p=str("".join(username))
                if n==50 and m==416:
                    username.append("A")
                    p=str("".join(username))
                if n==168 and m==416:
                    username.append("S")
                    p=str("".join(username))
                if n==286 and m==416:
                    username.append("D")
                    p=str("".join(username))
                if n==404 and m==416:
                    username.append("F")
                    p=str("".join(username))
                if n==522 and m==416:
                    username.append("G")
                    p=str("".join(username))
                if n==640 and m==416:
                    username.append("H")
                    p=str("".join(username))
                if n==758 and m==416:
                    username.append("J")
                    p=str("".join(username))
                if n==876 and m==416:
                    username.append("K")
                    p=str("".join(username))
                if n==994 and m==416:
                    username.append("L")
                    p=str("".join(username))
                if n==1112 and m==416:
                    username.append("/")
                    p=str("".join(username))
                if n==50 and m==534:
                    username.append("Z")
                    p=str("".join(username))
                if n==168 and m==534:
                    username.append("X")
                    p=str("".join(username))
                if n==286 and m==534:
                    username.append("C")
                    p=str("".join(username))
                if n==404 and m==534:
                    username.append("V")
                    p=str("".join(username))
                if n==522 and m==534:
                    username.append("B")
                    p=str("".join(username))
                if n==640 and m==534:
                    username.append("N")
                    p=str("".join(username))
                if n==758 and m==534:
                    username.append("M")
                    p=str("".join(username))
                if n==876 and m==534:
                    username.append("_")
                    p=str("".join(username))
                
            if n>=994 and m==534 and len(p)>0:
                yourturn.play()
                yourturn.rewind()
                player.playername()
                usernameflag = 0
                instructioncontroller = 1
                counter = 0
            
    
    if instructioncontroller == 1:
        if keyCode == SHIFT and counter>0:
            enterthegame.play()
            enterthegame.rewind()
            for c in range(spaceship.lives):
                lifes.append("[]")
            lifenum = "LIVES "+"".join(lifes)
            instructioncontroller = 0
            gamecontroller = 1
            thermometerflag= 1
            counter = 0
            openningcontroller = 0
            scoreboard = "SCORE   "+str(shoot_down)
            levelnum = "LEVEL   "+str(levels)
            bombnumber = "Bombs  "+str(bomb.bombnum-1)
            shoot_down = 0
            numberofcrashed=0
            sumlevel = 0
            levels = 1
            numberofasteriods = 3
            rocks=[]
            bullets=[]
            for x in range(numberofasteriods):
                rocks.append(Asteroid())
            shipalive_or_dead = 1    
            spaceship.x = width/2
            spaceship.y = height/2
            spaceship.direction =180

    
    if gamecontroller == 1:
        if key == "w":
            spaceshipmove = 1
            #print "11"
        if key == "d":
            spaceshipright = 1
        if key == "a":
            spaceshipleft = 1
        # print "12"
        if key == " " and counter >0 and cooldownflag == 0:
            laser.play()
            laser.rewind()
            heatflag = 1
            bullets.append(Bullet())
        if keyCode == SHIFT and counter>150:
            circlesize = 1
            bombactive = 1
            bomb.bombnum -= 1
            bomb.bomb_active()  
            if bomb.bombnum < 1:
                bombactive = 0 
                bomb.bombnum = 1
            else:
                bombsound.play()
                bombsound.rewind()
            bombnumber = "Bombs  "+str(bomb.bombnum-1)
        if key == "s":
            spaceship.x = random.randint(0,1280)
            spaceship.y = random.randint(0,720)
            
def keyReleased():
    global spaceshipright, spaceshipleft, spaceshipmove,heatflag,heat
    if key == "w":
        spaceshipmove = 0
    if key == "d":
        spaceshipright = 0
    if key == "a":
        spaceshipleft = 0
    if key == " ":
        heat = 0
        heatflag = 0
        
        