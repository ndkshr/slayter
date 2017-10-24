import pygame,random,time,math,winsound

pygame.init()
screen=pygame.display.set_mode((400,600))


sprite_image=[]

for i in range(5):
    sprite_image.append(pygame.image.load("demons/%d.png"%(i)))
    
pygame.display.set_caption("SLAYTER")

sprite_list=[]
frames=pygame.time.Clock()
background=pygame.image.load("background.png")
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

"""
sprite list



"""

def message(msg,color,x,y,size=28,font="Lemiesz.ttf"):
    font=pygame.font.SysFont(font,size)    
    text=font.render(msg,1,color)
    screen.blit(text,(x,y))

class exp:

    def __init__(self,X,Y):
        self.x,self.y=X,Y
        self.mag=1


class sprite:
    
    def __init__(self,index):

        self.index=index
        self.image_no=random.randrange(0,5)
        sizelist = [(50,50),(60,60),(150,30),(100,100),(150,150)]
        self.width,self.height = sizelist[self.image_no]
        
        self.pos_x,self.pos_y=(random.randrange(self.width,400)-self.width),random.randrange(-20,100)
        self.xc,self.yc=(random.randrange(self.width,400)-self.width),random.randrange(-20,100)
        self.theta=0
        self.dx=5
        self.dy=5
        self.dxc=5
        self.dyc=5
        self.hit_status=False
        self.hit_count=0
        self.movement=random.randrange(5)
        
        maxhitlist = [2,5,7,10,15] 
        
        self.max_hit = maxhitlist[self.image_no]
        self.flag=0

    def sprite_hit(self,mouse):

        """"""

        mx,my=pygame.mouse.get_pos()
        
        if self.pos_x <= mx <= (self.pos_x+self.width) and self.pos_y <= my <= (self.pos_y+self.height) and mouse=="down":
            self.hit_count+=1

        if self.hit_count >= self.max_hit:
            self.hit_status = True

        return self.hit_status

    def sprite_disp(self):
        screen.blit(sprite_image[self.image_no],(self.pos_x,self.pos_y))
        
    def sprite_motion(self):

        if self.movement==0: ########## rotational
            
            self.pos_x,self.pos_y,self.theta,self.xc,self.yc=rotational(self.xc,self.yc,self.theta,50,0.2)
            
        elif self.movement==1:######### horizontal
            self.pos_x,self.pos_y,self.xc,self.theta,self.dxc=horizontal(self.pos_x,50,self.xc,self.theta,self.dxc)
            
        elif self.movement==2: ######## vertical
            self.pos_x,self.pos_y,self.xc,self.yc,self.theta,self.dxc=vertical(50,self.xc,self.yc,self.theta,self.dxc)
            
        elif self.movement==3: ######## rotate_oscillate
            self.pos,self.pos_y,self.theta,self.xc,self.yc,self.dx=rotate_oscillate(self.xc,self.yc,self.theta,50,self.dx,0.2)
            
        elif self.movement==4: ######## line  generator
            self.pos_x,self.pos_y,self.flag=line_creator(self.pos_x,self.pos_y,self.flag)
            
    def datadisp(self):

        print "# no ",self.index
        print "image number ",self.image_no
        print "x= ",self.pos_x," y= ",self.pos_y
        print "hit count ",self.hit_count
            
"""
MOTION TYPES ARE
1 ROTATIONAL(circular)          (done)        round  , square  ,  star , quad
2 HORIZONTAL OSCILLATION         (done)       round , square , long 
3 VERTICAL OSCILLATION           (done)       round , square  , long
4 RANDOM LINE GENERATOR          (done)      round ,  square   
5 ROTATION + OSCILLATION          (done)      star , quad

"""



    
    

def rotational(xc,yc,angle,amp,i=1):

    """################### example ####################################"""
    ##    xpos,ypos,theta=rotational(xc,yc,theta,50,0.2)
    """################################################################"""
    
    print "in rot"
    angle+=i
    
    dy = random.randrange(1,4)
    yc=yc+dy
    
    return int(amp*math.cos(angle)+xc),int(amp*math.sin(angle)+yc),angle,xc,yc
    

def horizontal(ypos,amp,xc,angle,dxc):

    """################### example ####################################"""
##            xpos,ypos=0,0
##            xc=0
##            yc=0
##            dx=3
##            dxc=2
##            xpos,ypos,xc,theta,dxc=horizontal(ypos,50,xc,theta,dxc)
    """################################################################"""
    
    print "in horizontal"
    angle=angle+0.5
    
    if xc<=-1 or xc>=400:
        dxc*=-1

    xc+=dxc
    ypos+=0.5
    xpos = int(amp*math.cos(angle)+xc)
    
    return xpos,ypos,xc,angle,dxc



def vertical(amp,xc,yc,angle,dxc):
    """################### example ####################################"""

    ##            xc=0
    ##            yc=0
    ##            dx=3
    ##            dxc=2
    ##            xpos,ypos,xc,yc,theta,dxc=vertical(50,xc,yc,theta,dxc)
    """################################################################"""
    

    print "in vertical"
    angle=angle+0.5
    if xc<=-1 or xc>=400:
        dxc*=-1
        
    xc+=dxc
    yc+=1
    ypos = int(amp*math.sin(angle)+yc)
    xpos =  int(xc)

    return xpos,ypos,xc,yc,angle,dxc
    

def rotate_oscillate(xc,yc,angle,amp,dx,i=1):

    """################### example ####################################"""
    ##    xpos,ypos,theta,xc,yc,dx=rotate_oscillate(xc,yc,theta,50,dx,0.2)
    """################################################################"""
    
    print "in rot+osc"
    angle+=i
    
    if xc<=0: dx=3
    if xc>=400: dx=-3
    
    xc+=dx
    yc+=1
    return int(amp*math.cos(angle)+xc),int(amp*math.sin(angle)+yc),angle,xc,yc,dx



def line_creator(xpos,ypos,flag=0,dx=0,dy=0):

###################################################################
    if random.randrange(0,3)==2:
        if xpos>=400:
            flag =1

        
            
        elif xpos<=0:
            flag=0

        if not flag:  # touches left wall
            dx = random.randrange(-10,0)
            dy = random.randrange(-10,6)
        else:         # touches right wall
            dx = -1
            

###################################################################
    else:
        if xpos>=400:
            flag =1

        
            
        elif xpos<=0:
            flag=0

        if not flag:
            dx = random.randrange(0,10)
            dy = random.randrange(-4,10)
        else:
            dx = random.randrange(-10,-1)
            dy = random.randrange(-4,10)
###################################################################

    xpos+=dx
    ypos+=dy
    return xpos,ypos,flag
"""################################################################"""




    
def new_sprite(demon):
    
    """"""
    sprite_list.append(demon)






def sprites_update(mouse,exp_list,SCORE=0,health=100):


    for demon in sprite_list:
        demon.sprite_motion()
        demon.sprite_disp()
        
        if demon.sprite_hit(mouse):
            SCORE+=10*demon.max_hit
            exp_list.append(exp(demon.pos_x+int(demon.width/2),demon.pos_y+int(demon.height/2)))
            sprite_list.remove(demon)
            
            
        elif (demon.pos_y+demon.height)>=500:
            health=health-2*demon.max_hit
            exp_list.append(exp(demon.pos_x+int(demon.width/2),demon.pos_y+int(demon.height/2)))
            sprite_list.remove(demon)
            
            
    for d in sprite_list:
        d.datadisp()
        
    return SCORE,health,exp_list
    

def explode(exp_list):
    clr=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255)]
    for e in exp_list:
        if e.mag==1:
            snd=pygame.mixer.music.load("sound/bubble pop.wav")
            pygame.mixer.music.play()
            #winsound.PlaySound("sound/JewelBeat - Game Player.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        if e.mag<50:
            exp_x = e.x + random.randrange(-1*e.mag,e.mag)
            exp_y = e.y + random.randrange(-1*e.mag,e.mag)
            pygame.draw.circle(screen,clr[random.randrange(0,5)],(int(exp_x),int(exp_y)),random.randrange(5,10))
            e.mag+=1
        elif e.mag==50:
            exp_list.remove(e)

def if_quit():
    pygame.mouse.set_visible(1)
    out = False
    mouse_down = False
    col_yes = (0,255,0)
    col_no = (255,0,0)
    BG = pygame.image.load("is_quit()/BG.png")
    NO = pygame.image.load("is_quit()/NO.png")
    YES = pygame.image.load("is_quit()/YES.png")
    while not out:
        for event in pygame.event.get():
            print event

            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                out=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False
            
        x,y=pygame.mouse.get_pos()


        pygame.draw.rect(screen,(255,255,255),pygame.Rect(50,200,300,150))
        screen.blit(BG,(50,200)) 
        if 100 <= x <= 160 and 300 <= y <= 330:
            pygame.draw.rect(screen,(0,255,0),[100,300,60,30])
            if(mouse_down):
                out=True
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen,(255,255,255),[100,300,60,30])
        
        
        if 240 <= x <= 300 and 300 <= y <= 330:
            pygame.draw.rect(screen,(255,0,0),[240,300,60,30])
            if mouse_down:
             out = True
            
        else:
           pygame.draw.rect(screen,(255,255,255),[240,300,60,30])

           
        screen.blit(YES,(100,300))
        screen.blit(NO,(240,300))
        

        pygame.display.update()
    return not out    

def healthbar(health,x=0,y=450):
    
    
    barwidth=health*4
    c=green
    if 75<=health<=100:
        c=green
    elif 50<=health<=74:
        c=blue
    elif 0<=health<=49: c=red
    pygame.draw.rect(screen,black,[x,y,400,14])
    pygame.draw.rect(screen,c,[x,y+2,barwidth,10])
    

def toolbar(health,TOOL,x=0):
    pygame.mouse.set_visible(1)
    y=450
    lm,sm,rm=0,0,0
    flag=0
    clr=(255,255,0)
    img=pygame.image.load("user_items/main toolbar.png")
    run=True
    while run:

        for event in pygame.event.get():
            print event
            lm,sm,rm=pygame.mouse.get_pressed()
            
            if event.type==pygame.QUIT:
                run=if_quit()
                if not run:
                 pygame.quit()
                 exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 4:
                    flag=1
                elif event.button == 5:
                    flag=-1
                else:
                    flag=0

            if rm:
                run=False
                

                
        mx,my=pygame.mouse.get_pos()
        if 25<mx<125 and 475<my<575:
            clr=(0,255,0)
            if lm:
                if x==0:
                    TOOL="punch"
                if x==-125:
                    TOOL="hammer"
                if x==-250:
                    TOOL="axe"
                if x==-375:
                    TOOL="sword"
                if x==-500:
                    TOOL="bomb"
                if x==-625:
                    TOOL="painkiller"
                print TOOL
                run=False
                    
        else:
            clr=(255,255,0)
        pygame.draw.rect(screen,(0,0,0),[0,450,400,150])    
        pygame.draw.circle(screen,clr,(75,600-75),50)
        pygame.draw.circle(screen,(255,255,255),(200,600-75),50)
        pygame.draw.circle(screen,(255,255,255),(325,600-75),50)
        
        if flag==1 and x>=-600:
            x=x-125
        screen.blit(img,(x,y))
        pygame.display.update()

        if flag==-1 and x:
            x=x+125
        
        screen.blit(img,(x,y))
        pygame.display.update()
            
        flag=0
        healthbar(health,0,450-14)
        pygame.display.update()
    print "out of toolbar"
    return (x),not rm,TOOL
            
def tooldisplay(TOOL):
    """"""
    i=pygame.image.load("user_items/beginner/%s.png"%TOOL)
    mx,my=pygame.mouse.get_pos()
    screen.blit(i,(mx-15,my-15))
    pygame.mouse.set_visible(0)

def scoreboard(SCORE):
    """"""
    message("SCORE : %d"%SCORE,(0,0,0),140,550)
    

def if_GAMEOVER(health):
    if health<=0:
        message("GAME OVER!!!!",(0,0,0),120,300,50,"slaytanic")
        pygame.display.update()
        time.sleep(2)
##        pygame.quit()
##        exit()
        import startpage


def pauseGAME():
    i=3
    while True:
        pygame.event.get()
        pressed=pygame.key.get_pressed()
        
        if pressed[pygame.K_r] or i<3:
            screen.blit(background,(0,0))
            message("-: GAME STARTS IN :-",(0,0,0),70,220,40,"slaytanic")
            message("%d"%i,(0,0,0),200,300,60)
            pygame.display.update()
            time.sleep(1)
            i-=1
            if i==0:
                return 0
        else:
            message("P A U S E D",(0,0,0),130,250,40,"slaytanic")
            pygame.display.update()



    
def main_game():
    bomb_count=3
    running=True
    sINDEX=0
    mouse="up"
    SCORE,health=0,100
    x=4.0
    theta=0
    TOOL="punch"
    tx=0
    lm,sm,rm=0,0,0
    start_time=time.time()

    exp_list = []

    winsound.PlaySound("sound/JewelBeat - Game Player.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    while running:
        for event in pygame.event.get():

            print event

            if event.type==pygame.QUIT:
                if_quit()
                
                

            if event.type==pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button==1:
                    mouse="down"
            if event.type==pygame.MOUSEBUTTONUP:
                mouse="up"
                
            lm,sm,rm=pygame.mouse.get_pressed()
            
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_p]:
            pauseGAME()
            
        screen.fill(white)
        screen.blit(background,(0,0))

        elapsed=time.time()-start_time
        if (x-1.0) <= elapsed <= x or elapsed>=x:
            new_sprite(sprite(sINDEX))
            start_time=time.time()
            print "start_time=",start_time
            sINDEX+=1
        
        SCORE,health,exp_list=sprites_update(mouse,exp_list,SCORE,health)
        
        explode(exp_list)
        scoreboard(SCORE)
        if SCORE<4000:
            x=5-float(SCORE/1000)
        
        if rm:
            tx,rm,TOOL=toolbar(health,TOOL,tx)

        else:
            healthbar(health,0,500)
            
        tooldisplay(TOOL)
        pygame.display.update()
        if_GAMEOVER(health)
        frames.tick(25)
        
    print sprite_list
    pygame.quit()
    quit()
##########################################################################

main_game()
