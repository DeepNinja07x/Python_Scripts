import pygame,sys
import time
import random

pygame.init() #Initializing PyGame Module

#Setting colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

#Setting boreders in px
window_width=800
window_height=600

gameDisplay=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Slither.io - The Snake Game')

clock=pygame.time.Clock()#varible for getting time within the program
FPS=5 #Frame_per_second 
blockSize=20
noPixel=0

def myquit():
    '''Self explanatory'''
    pygame.quit()
    sys.exit(0)
font=pygame.font.SysFont(None,35,bold=True)

def drawGrid():
    sizeGrd=window_width//blockSize

def snake(blockSize,snakelist):
    #x=250-(segment_width+segment_margin)*i
    for size in snakelist:
        pygame.draw.rect(gameDisplay,white,[size[0]+5,size[1],blockSize,blockSize],2)

def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[100,window_height/2])

def gameLoop():
    gameExit=False
    gameOver=False

    lead_x=window_width/2
    lead_y=window_height/2

    change_pixels_of_x=0
    change_pixels_of_y=0
    snakelist = []
    snakeLength = 1
    randomAppleX = int(random.randrange(0, window_width-blockSize)/10)*10
    randomAppleY = int(random.randrange(0, window_height-blockSize)/10)*10

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over, press 'c' to play again or 'q' to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                    
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True                   

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        gameDisplay.fill(black)
        AppleThickness = 20

        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.circle(gameDisplay, red, [randomAppleX,randomAppleY],10)

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]        

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True             

        snake(blockSize, snakelist)     
        pygame.display.update()
        
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = int(random.randrange(0, window_width-blockSize)/10)*10
                randomAppleY = int(random.randrange(0, window_height-blockSize)/10)*10
                snakeLength += 1             

        clock.tick(FPS)
        
    pygame.quit()
    quit()


gameLoop()
