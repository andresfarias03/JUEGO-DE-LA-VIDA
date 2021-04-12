import pygame
import numpy as np
import time

pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((height, width))

bg = 0, 0, 140
screen.fill(bg)

n = 0.1
nxC, nyC = 50, 50
 
dimCW = width / nxC
dimCH = height / nyC


gameState = np.zeros((nxC, nyC))

gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1


gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False

while True:
    
    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(n)
    
    ev = pygame.event.get()
    
    for event in ev:
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                pauseExect  = not pauseExect
            if event.key == pygame.K_RIGHT:
                n-=0.1
            if event.key == pygame.K_LEFT:
                n+=0.1
                
        mouseClick = pygame.mouse.get_pressed()
        #print(mouseClick)
        if sum(mouseClick) > 0:
               posX, posY = pygame.mouse.get_pos()
               celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
               newGameState[celX, celY] = not mouseClick[2]
             
    
    
    for y in range(0, nxC):
        for x in range(0, nyC):
            
            if not pauseExect:
            
            
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x)     % nxC, (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, (y)     % nyC] + \
                          gameState[(x + 1) % nxC, (y)     % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[(x)     % nxC, (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]
                
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                
            
            
            poly = [((x)   * dimCW, y * dimCH),
                   ((x+1) * dimCW, y * dimCH),
                   ((x+1) * dimCW, (y+1) * dimCH),
                   ((x)   * dimCW, (y+1) * dimCH)] 
            
           
            if newGameState[x, y] == 0:            
                  pygame.draw.polygon (screen, (128, 128, 128), poly, 1)
            else:
                  pygame.draw.polygon (screen, (0, 255, 255), poly, 0)
   
    gameState = np.copy(newGameState)
   
   
    pygame.display.flip() 
    
pygame.quit()
    
