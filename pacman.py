import pygame 


pygame.init()


WIDTH = 800
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60 # max speed at which game could be played. (no advantage even with high speed comp)
font = pygame.font.Font('freesansbold.ttf', 20)

run = True # game loop to execute the game
while run:
    timer.tick(fps) # frame rate which was defined earlier
    screen.fill('black') # solid bg color

#get out of the game
    for event in pygame.event.get(): #event game handler  
        if event.type ==pygame.QUIT:
            run = False 

    pygame.display.flip() # let everything that you draw on the screen, flip it 
pygame.quit()
