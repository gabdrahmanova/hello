import pygame
pygame.init()
display_width = 800
display_height = 600
carImg = pygame.image.load('розы.jpg')
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
crashed=False
go_left=False
i=0
x =  (display_width * 0.6)
y = (display_height * 0)	
white = (255,255,255) 
while not crashed:
    clock.tick(60)
    i=i+1
    if go_left==False:
        x=x+2
    else:
        x=x-2
    if x>display_width:
        go_left=True
        else:
            x=x+1
    if go_left=True>display_width:
        go_left==False
    print(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(white)
    gameDisplay.blit(carImg, (x,y))
    pygame.display.update()
