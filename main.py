import pygame
import asyncio

scale=1
screenWidth = 320
screenHeight= 320+180
screen = pygame.Surface((screenWidth, screenHeight))
fenetre = pygame.display.set_mode((scale*screenWidth, scale*screenHeight))#,pygame.SCALED)

pygame.display.set_caption('Gods')
pygame.init()
pygame.mouse.set_visible(True)

offsetH = 3
spH = 48
spW = 36

control = pygame.image.load('unnamed.png')
print (fenetre.get_rect().size)
print (control.get_rect().size)
newHeight = int(control.get_rect().size[1] / 640 * screenWidth)
print (newHeight)
control = pygame.transform.scale(control, (screenWidth,newHeight))

spritesheet = pygame.image.load('sprites.png')
spritesheet.set_colorkey(0XFF00FF)
sprite = [spritesheet.subsurface((x%4)*spW,offsetH+(x//4)*(spH+offsetH),spW,spH)for x in range(8)]

            
jouer = True
index_sprite = 0

#-------------
# 1/3 - LOOP
# async def main():
def main():
#-------------
    global jouer, index_sprite, sprite,newHeight
    while jouer:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jouer = False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            jouer=False
        
        # print (pygame.mouse.get_pos())
    
        #les 4 lignes pour afficher le sprite animé
        index_sprite = (index_sprite+1)%(len(sprite))
        screen.fill((255,255,255))
        screen.blit(sprite[index_sprite],(100,100))
        screen.blit(control,(0,screenHeight-newHeight))
        fenetre.blit(pygame.transform.scale(screen, fenetre.get_rect().size), (0, 0))
        
        pygame.display.flip()
        
        #-------------
        # 2/3 - WAIT
        # await asyncio.sleep(0)#.15)  # Let other tasks run    
        pygame.time.wait(10)
        #-------------

#-------------
# 3/3 - RUNEND
# asyncio.run(main())
main()
pygame.quit()
#-------------