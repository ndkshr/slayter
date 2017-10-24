import pygame,winsound,pickle
import time,os

pygame.init()

screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("SLAYTER")
background=pygame.image.load("background.png")
title= pygame.image.load("TITLE.png")
frames=pygame.time.Clock()
gameOver=False



##gameinfo=[0,0,0,0,0,[]]
#info_file=open("Data/gameinfo.txt","wb")

class game_info():
    
    def __init__(self):
        self.sound_var=0
        self.effect_var=0
        self.highScore=0
        self.total_score=0
        self.games_played=0
        self.average=0
        self.tools=[]

    def info_update(self):
        pickle.dump(self,open("Data/gameinfo.txt","wb"))
        


##############################################################################
########################### game info storage ################################
##############################################################################
        
st=game_info()
if os.path.exists("Data/gameinfo.txt"):
    st=pickle.load(open("Data/gameinfo.txt","rb"))
else:
    st.info_update()
    
##############################################################################




def message(msg,color,x,y,size=28,font="slaytanic"):
    font=pygame.font.SysFont(font,size)    
    text=font.render(msg,1,color)
    screen.blit(text,(x,y))

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
                st.info_update()
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




def logo_nk():

    
    logo = pygame.image.load("logo_nk/1.jpg")
    
    screen.blit(logo,(0,0))
    pygame.display.update()
        
    time.sleep(1)
    for i in range(1,9):
        
        logo = pygame.image.load("logo_nk/%d.jpg"%i)
        screen.blit(logo,(0,0))
        pygame.display.update()
        frames.tick(20)
        
    time.sleep(2)
    
    for i in range(8,0,-1):
        
        logo = pygame.image.load("logo_nk/%d.jpg"%i)
        screen.blit(logo,(0,0))
        pygame.display.update()
        frames.tick(20) 
    time.sleep(2)

    title = pygame.image.load("TITLE_color.png")
    bg = pygame.image.load("background.png")
    for i in range(100,0,-2):
        screen.blit(bg,(0,0))
        screen.blit(title,(0,i))
        pygame.display.update()
        frames.tick(100)

    
    #time.sleep(1)    


def sound_settings(svar=0,evar=0):


    back_var=False
    mouse_down=False
    back=pygame.image.load("press/back.png")
    while not back_var:
        
        for event in pygame.event.get():
            print event

            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                out=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False

        x_pos,y_pos=pygame.mouse.get_pos()

        #                           """THE BUTTON STATE CHANGES ON HOVER MOTION OF MOUSE """    


        if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
            back = pygame.image.load("pressed/back.png")
            if(mouse_down):
                back_var=True
        else:
                back = pygame.image.load("press/back.png")

        
        screen.blit(background,(0,0))
        screen.blit(back,(10,10))
        
        message(" m u s i c ",(0,0,0),100,200)
        pygame.draw.rect(screen,(0,255,0),[280,200,50,20])
        if svar:
            pygame.draw.rect(screen,(0,0,255),[280+25,200,25,20])

        message("e f f e c t",(0,0,0),100,400)
        pygame.draw.rect(screen,(0,255,0),[280,400,50,20])
        if evar:
            pygame.draw.rect(screen,(0,0,255),[280+25,400,25,20])
        
        pygame.display.update()        
        frames.tick(20)


00000000#*****************************************************************************************
#                                   {INSIDE SETTINGS}
#*****************************************************************************************



def Credits():
    """"""




def in_settings(no):
    mouse_down=False
    if(no==1):
        
        print"control"
        b=pygame.image.load("press/back.png")
        inst=pygame.image.load("INSTRUCTION.png")
        back_var=False
        while(not back_var):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    back_var=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_down=True
                if event.type==pygame.MOUSEBUTTONUP:
                    mouse_down=False

                    
            x_pos,y_pos=pygame.mouse.get_pos()
            if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
                b=pygame.image.load("pressed/back.png")
                if(mouse_down):
                    back_var=True
            else:
                b=pygame.image.load("press/back.png")

            screen.blit(inst,(0,0))
            screen.blit(b,(10,10))
            pygame.display.update()
                    
    elif(no==2):
        print"sounds"
        sound_settings()
    elif(no==3):
        print "credits"
    

def statistics(highscore_icon):
    """"""
    b=pygame.image.load("press/back.png")
    back_var=False
    while(not back_var):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                back_var=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False

                
        x_pos,y_pos=pygame.mouse.get_pos()
        
        if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
            b=pygame.image.load("pressed/back.png")
            if(mouse_down):
                back_var=True
        else:
            b=pygame.image.load("press/back.png")

        
        screen.blit(background,(0,0))
        screen.blit(b,(10,10))
        message("s t a t i s t i c s",(0,0,0),240-80,91)
        screen.blit(highscore_icon,(200-25-80,100-25))
        message("B E S T                    %d"%(st.highScore),(0,0,0),80,200,30,"Lemiesz.ttf")
        
        message("T O T A L                 %d"%(st.total_score),(0,0,0),80,300,30,"Lemiesz.ttf")
        message("GAMES PLAYED      %d"%(st.games_played),(0,0,0),80,400,30,"Lemiesz.ttf")
        message("A V E R A G E           %d"%(st.average),(0,0,0),80,500,30,"Lemiesz.ttf")
        pygame.display.update()




##**************************************************************************************
##                      SETTINGS
##**************************************************************************************
def settings(settings_icon):                                                      
    print"inside settings"
    back_var=False
    mouse_down=False
   
    controls = pygame.image.load("press/controls.png")
    credit = pygame.image.load("press/credits.png")
    back=pygame.image.load("press/back.png")
    sound = pygame.image.load("press/sound.png")

    while not back_var:
        
        for event in pygame.event.get():
            print event

            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                out=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False

        x_pos,y_pos=pygame.mouse.get_pos()

        #                           """THE BUTTON STATE CHANGES ON HOVER MOTION OF MOUSE """    


        if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
            back = pygame.image.load("pressed/back.png")
            if(mouse_down):
                back_var=True
        else:
                back = pygame.image.load("press/back.png")
    
        if 300-25 < y_pos < 300+25 and 200-25 < x_pos < 200+25:
                controls = pygame.image.load("pressed/controls.png")
                if(mouse_down):
                    in_settings(1)
                    
        else:
                controls = pygame.image.load("press/controls.png")
                
        if 400-25 < y_pos < 400+25 and 200-25 < x_pos < 200+25:
                sound = pygame.image.load("pressed/sound.png")
                if(mouse_down):
                    in_settings(2)
                    
        else:
               sound = pygame.image.load("press/sound.png")
                
        if 500-25 < y_pos < 500+25 and 200-25 < x_pos < 200+25:
                credit = pygame.image.load("pressed/credits.png")
                if(mouse_down):
                    in_settings(3)
                    
        
        else:
                 credit = pygame.image.load("press/credits.png")

        screen.blit(background,(0,0))
        screen.blit(back,(10,10))
        screen.blit(settings_icon,(200-25-80,100-25))
        screen.blit(controls,(200-25,300-25))
        screen.blit(sound,(200-25,400-25))
        message("s e t t i n g s",(0,0,0),240-80,91)
        screen.blit(credit,(200-25,500-25))

        pygame.display.update()        
        frames.tick(20)


##********************************************************************************************
##********************************************************************************************

def play_START():

    inplay=True
    back_var=False
    back=pygame.image.load("press/back.png")
    mouse_down=False
    pclr=(0,255,100)
    iclr=(74,178,230)
    giclr=(0,0,0)
    gpclr=(0,0,0)
    while not back_var:
        
        for event in pygame.event.get():
            print event

            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                out=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False

        x_pos,y_pos=pygame.mouse.get_pos()

        
        
        if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
            back = pygame.image.load("pressed/back.png")
            if(mouse_down):
                back_var=True
        else:
                back = pygame.image.load("press/back.png")
        

        if 200 < y_pos < 250 and 150 < x_pos < 250:
            pclr=(111,255,2)
            gpclr=(110,115,107)
            if(mouse_down):
                print("play_start")
                import maingame
                #maingame.main_game()
                #os.system("python maingame.py")
        else:
                pclr=(169,245,111)
                gpclr=(0,0,0)


        if 400 < y_pos < 450 and 120 < x_pos < 280:
            iclr=(0,205,255)
            giclr=(110,115,107)
            if(mouse_down):
                print("instr")
                bv=False
                while not bv:
                    for event in pygame.event.get():
                        print event

                        if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                            out=True

                        if event.type==pygame.MOUSEBUTTONDOWN:
                            mouse_down=True
                        if event.type==pygame.MOUSEBUTTONUP:
                            mouse_down=False

                    x_pos,y_pos=pygame.mouse.get_pos()

                    
                    
                    if 10 < y_pos < 10+50 and 10 < x_pos < 10+50:
                        back = pygame.image.load("pressed/back.png")
                        if(mouse_down):
                            bv=True
                    else:
                            back = pygame.image.load("press/back.png")

                            
                    screen.blit(background,(0,0))
                    screen.blit(back,(10,10))
                    message("I N S T R U C T I O N S",(0,0,0),100,50,30)
                    message("(1) The purpose is to click on the demons",(0,0,0),10,130,28,"Lemiesz.ttf")
                    message("      and kill them.",(0,0,0),10,160,28,"Lemiesz.ttf")
                    message("(2) Score points and coins to,use them",(0,0,0),10,190,28,"Lemiesz.ttf")
                    message("     upgrade your Arsenal of weapons.",(0,0,0),10,220,28,"Lemiesz.ttf")
                    message("(3) Gain experience and points to improve",(0,0,0),10,250,28,"Lemiesz.ttf")
                    message("     your gaming experience.",(0,0,0),10,280,28,"Lemiesz.ttf")
                    message("(4) For more info on control & specs goto",(0,0,0),10,310,28,"Lemiesz.ttf")
                    message("     settings and find more",(0,0,0),10,340,28,"Lemiesz.ttf")
                    message("(5) Have A Great GAME!!!!!!",(0,0,0),10,370,28,"Lemiesz.ttf")
                    pygame.display.update()



                    
        else:
                iclr=(74,178,230)
                giclr=(0,0,0)
        
        screen.blit(background,(0,0))

        
        pygame.draw.rect(screen,gpclr,[150,200,100,50])
        pygame.draw.rect(screen,pclr,[154,204,92,42])
        message("play",gpclr,175,207,30)

        
        pygame.draw.rect(screen,giclr,[120,400,160,50])
        pygame.draw.rect(screen,iclr,[124,404,152,42])
        message("instructions",giclr,130,407,30)
        
        screen.blit(back,(10,10))
        pygame.display.update()

                
    

##******************************************************************************************
##                              START MENU
##******************************************************************************************

def start_menu():
    pygame.mouse.set_visible(1)
    logo_nk()
    out=False
    play=False

    play_icon = pygame.image.load("press/play.png")
    highscore_icon = pygame.image.load("press/highscore.png")
    settings_icon = pygame.image.load("press/settings.png")
    quit_icon = pygame.image.load("press/quit.png")
    mouse_down=False
    winsound.PlaySound("sound/JewelBeat - Game Player.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

    
    while not out:

        for event in pygame.event.get():
            print event
        
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                out=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_down=False

            
        x_pos,y_pos=pygame.mouse.get_pos()
        

        #                           """THE BUTTON STATE CHANGES ON HOVER MOTION OF MOUSE """

        if y_pos<150:
            title= pygame.image.load("TITLE_color.png")

        else:
            title= pygame.image.load("TITLE.png")
        
        if 200-25 < y_pos < 200+25 and 200-25 < x_pos < 200+25:
                play_icon = pygame.image.load("pressed/play.png")
                if(mouse_down):
                    print"play"
                    play_START()
        else:
                play_icon = pygame.image.load("press/play.png")
                
        if 300-25 < y_pos < 300+25 and 200-25 < x_pos < 200+25:
                highscore_icon = pygame.image.load("pressed/highscore.png")
                if(mouse_down):
                    print"highscore"
                    statistics(highscore_icon)
        else:
                highscore_icon = pygame.image.load("press/highscore.png")
                
        if 400-25 < y_pos < 400+25 and 200-25 < x_pos < 200+25:
                settings_icon = pygame.image.load("pressed/settings.png")
                if(mouse_down):
                    print"settings"
                    settings(settings_icon)
                    print"back from settings"
        else:
               settings_icon = pygame.image.load("press/settings.png")
                
        if 500-25 < y_pos < 500+25 and 200-25 < x_pos < 200+25:
                 quit_icon = pygame.image.load("pressed/quit.png")
                 if(mouse_down):
                    # game exits here
                     if_quit()
                     
        
        else:
                 quit_icon = pygame.image.load("press/quit.png")


        screen.blit(background,(0,0))
        screen.blit(title,(0,0))
        screen.blit(play_icon,(200-25,200-25))
        screen.blit(highscore_icon,(200-25,300-25))
        screen.blit(settings_icon,(200-25,400-25))
        screen.blit(quit_icon,(200-25,500-25))
        
        
        pygame.display.update()        
        frames.tick(20)


    st.info_update()
    pygame.quit()
    quit()
        
##********************************************************************************************
##********************************************************************************************
    
def main():

    start_menu()

##********************************************************************************************
##********************************************************************************************

    

##############################################################################################
##                                            MAIN

main()

##############################################################################################



