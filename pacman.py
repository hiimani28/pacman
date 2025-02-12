import pygame 
from board import boards
import math
pygame.init()


WIDTH = 700
HEIGHT = 750
PI = math.pi
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60 # max speed at which game could be played. (no advantage even with high speed comp)
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards # can create more levels of different difficulty levels and just import it based on the list 
color = 'blue'
player_images = []
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'),(30,30)))
player_x = 260
player_y =  500
direction = 0 
counter = 0 
flicker = False
def draw_board(): 
    num1 = ((HEIGHT - 50)//32) # how tall each piece of the board should be. 
    num2 = (WIDTH//30) # 30 horizontal blocks 
    for i in range(len(level)): # for loop fo revery row
        for j in range(len(level[i])): # iterates every col inside that row 
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j*num2+ (0.5*num2), i*num1 +(0.5*num1)),3)    # little black dots, j*num2 (x coordinate,)
                # surface, location, xy coordinates and radius =3. This creates the small circles 
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j*num2+ (0.5*num2), i*num1 +(0.5*num1)),7)

            if level[i][j] == 3: # horizontal lines
                pygame.draw.line(screen,color,(j*num2 + (0.5*num2), i*num1), # x coordinate for line
                                (j*num2 + (0.5*num2), i*num1 + num1), 2  ) # y coordinate, from the top to the bottom of the square --> i*num1 + num1. 
                
            if level[i][j] == 4: # vertical lines 
                pygame.draw.line(screen,color,(j*num2, i*num1+(0.5*num1)), 
                                (j*num2 + num2, i*num1 + (0.5*num1)), 2 )
                
            if level[i][j] == 5: # left arc
                pygame.draw.arc(screen, color, [(j*num2  - (num2*0.4)) - 2, (i*num1 + (0.5*num1)), num2, num1],0, PI/2, 2)
                # A full circle is 0 to 2PI (radiance), but for arc its going to be 1/4th of a circle, which is basically pi/2
            
            if level[i][j] == 6: # right arc
                pygame.draw.arc(screen, color, [(j*num2  + (num2*0.5)) , (i*num1 + (0.5*num1)), num2, num1],PI/2, PI, 2)
            
            if level[i][j] == 7: 
                pygame.draw.arc(screen, color, [(j*num2  + (num2*0.5)), (i*num1 - (0.4*num1)), num2, num1],PI, 3*PI/2, 2)
            
            if level[i][j] == 8: 
                pygame.draw.arc(screen, color, [(j*num2  - (num2*0.4)) -2 , (i*num1 - (0.4*num1)), num2, num1],3*PI/2, 2*PI, 2)
            

            if level[i][j] == 9: # white horizontal line
                pygame.draw.line(screen,'white',(j*num2, i*num1+(0.5*num1)), # vertical lines 
                    (j*num2 + num2, i*num1 + (0.5*num1)), 3  ) 

def draw_player():
    if direction == 0: # right
        screen.blit(player_images[counter//5],(player_x,player_y))
    elif direction == 1: #left
        screen.blit(pygame.transform.flip(player_images[counter//5], True, False),(player_x,player_y))
    elif direction == 2: # down
        screen.blit(pygame.transform.rotate(player_images[counter//5],90),(player_x,player_y))
    elif direction == 3: # up
        screen.blit(pygame.transform.rotate(player_images[counter//5], 270),(player_x,player_y))


run = True # game loop to execute the game
while run:
    timer.tick(fps) # frame rate which was defined earlier
    if counter <19: # how fast he animates.
        counter +=1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True


    screen.fill('black') # solid bg color
    draw_board()
    draw_player()

#get out of the game
    for event in pygame.event.get(): #event game handler  
        if event.type ==pygame.QUIT:
            run = False 
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction= 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
        


    pygame.display.flip() # let everything that you draw on the screen, flip it 
pygame.quit()
