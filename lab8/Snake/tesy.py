import pygame
pygame.init()
screen=pygame.display.set_mode((600, 300))
running=True
square=
while running:
    pygame.draw.circle(screen,'Red',(100,200),20)
   
    pygame.display.update()
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()