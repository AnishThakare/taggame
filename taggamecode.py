
#importing things
import os
import pygame
import pygame.draw_py
#main control variables
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
run = True
dt = 0
startvariable = False

#importing and scaling clicktoplay screen, background,runner,and tagger respectively
clicktoplayscreensmall = pygame.image.load(os.path.join('clicktoplayasset.png'))
clicktoplayscreen = pygame.transform.scale(clicktoplayscreensmall,(1280,720))
backgroundsmall = pygame.image.load(os.path.join('backgroundasset.png'))
background = pygame.transform.scale(backgroundsmall,(1280,720))
runnersmall = pygame.image.load(os.path.join('runnerasset.png'))
runner = pygame.transform.scale(runnersmall,(80,80))
runnerrect = runner.get_rect()
taggersmall = pygame.image.load(os.path.join('taggerasset.png'))
tagger = pygame.transform.scale(taggersmall,(80,80))
taggerrect = tagger.get_rect()
taggametitlesmall = pygame.image.load(os.path.join('taggametitleasset.png'))
taggametitle = pygame.transform.scale(taggametitlesmall,(256,144))

#runner and tagger coordinates respectively
runnerrect.x = screen.get_width() / 3
runnerrect.y = screen.get_height() / 2
taggerrect.x = screen.get_width() *2 / 3
taggerrect.y = screen.get_height() / 2

#setting up the text
pygame.display.set_caption(' tag game')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('WASD for runner Arrow keys for tagger', True, "black", "white")
textRect = text.get_rect()
textRect.center = ( 640,180)

#stating runner and tagger speed respectively
rs = 12
ts = 18

#making the mouse visible
pygame.mouse.set_visible(True)

#defining functions
def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        runnerrect.y -= rs
    if keys[pygame.K_s]:
        runnerrect.y += rs
    if keys[pygame.K_a]:
        runnerrect.x -= rs
    if keys[pygame.K_d]:
        runnerrect.x += rs
    if keys[pygame.K_UP]:
        taggerrect.y -= ts
    if keys[pygame.K_DOWN]:
        taggerrect.y += ts
    if keys[pygame.K_LEFT]:
        taggerrect.x -= ts
    if keys[pygame.K_RIGHT]:
        taggerrect.x += ts
while run:
    quit_game()
    movement()
    screen.blit(clicktoplayscreen,(0,0))
    if pygame.mouse.get_pressed()[0]:
        startvariable = True
        startvariable2 = True
    if startvariable:
            if startvariable2:
                runnerrect.x = screen.get_width() / 3
                runnerrect.y = screen.get_height() / 2
                taggerrect.x = screen.get_width() *2 / 3
                taggerrect.y = screen.get_height() / 2
                startvariable2 = False

            screen.blit(background,(0,0))
            screen.blit(runner,(runnerrect.x,runnerrect.y))
            screen.blit(tagger,taggerrect)
            screen.blit(text, textRect)
            screen.blit(taggametitle,(512,20))
            
        
    #tagging if statement
    if pygame.Rect.colliderect(taggerrect, runnerrect):
        startvariable = False
            
    #flipping the code
    pygame.display.flip()
    #setting FPS
    dt = clock.tick(30) / 1000

pygame.quit()
