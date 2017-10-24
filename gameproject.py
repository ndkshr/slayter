import pygame,random,time,math

pygame.init()

screen=pygame.display.set_mode((400,600))

pygame.display.set_caption("GAME PROJECT BETA VERSION")

frames=pygame.time.Clock()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

class sprite:
    def __init__(self,t,posx,posy,width,height):

        self.image=t
        self.posx,self.posy=posx,posy
        self.dimension=(width,height)
        
    def display(self):

        screen.blit(image,(x,y))
        pygame.display.update()

    def hit(self):

        x,y=pygame.mouse.get_pos()
        hit=False
        if posx <= x <= (posx+width) and posy <= y <= (posy+height):
            hit = True

        return hit    
            
        
    
def user_items():

    """LOAD ALL THE IMAGES OF USER ITEMS"""

    
    
    

def if_quit():

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
    return out    

def healthbar(health):
    print "health"
    barwidth=health*6
    c=green
    if 75<=health<=100:
        c=green
    elif 50<=health<=74:
        c=blue
    elif 0<=health<=49: c=red
    pygame.draw.rect(screen,black,[0,450,600,14])
    pygame.draw.rect(screen,c,[0,452,barwidth,10])
    


def toolbar(health):

    run=True
    
    while run:
        
        for event in pygame.event.get():

            print event
            
            if event.type==pygame.QUIT:
                if if_quit():
                    return
                
            
        pygame.draw.rect(screen,(211,252,10),[0,450,400,600-450])
        pygame.draw.circle(screen,green,(200,450+15+60),60)
        healthbar(health)
        pygame.display.update()
        



def main_game():

    running=True
    img=pygame.image.load("demons/round_demon.png")
    
    health=100
    background=pygame.image.load("background.png")

    
    theta=0
    while running:
        for event in pygame.event.get():

            print event

            if event.type==pygame.QUIT:
                running=False

            
        screen.fill(white)
        screen.blit(background,(0,0))
        
        screen.blit(img,(200+50*math.cos(theta*3.14/180),200+50*math.sin(theta*3.14/180)))
        theta=theta+1    
        toolbar(health)
        pygame.display.update()
        frames.tick(15)
        

    pygame.quit()
    quit()

    

main_game()
