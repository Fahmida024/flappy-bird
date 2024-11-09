import pygame
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
fps=60
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption('Flappy bird')
ground_scroll=0
scroll_speed=4
playing=True

bird1=pygame.image.load('bird1.png')
bird2=pygame.image.load('bird2.png')
bird3=pygame.image.load('bird3.png')

background=pygame.image.load('backgroundimg.png')
ground=pygame.image.load('ground.png')
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[bird1,bird2,bird3]
        self.index=0
        self.counter=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
    def update(self):
        self.vel=self.vel+0.01
        if self.vel>8:
            self.vel=8
        if self.rect.bottom<650:
            self.rect.y+=int(self.vel)
        #detecting left click
        if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
            self.vel=-10
            self.clicked=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked==False
        self.counter=self.counter+1
        if self.counter>5:
            self.counter=0
            self.index+=1
            if self.index>2:
                self.index=0
        self.image=self.images[self.index]

bird_group=pygame.sprite.Group()
flappy=Bird(100,250)
bird_group.add(flappy)


while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    clock.tick(fps)
    screen.blit(background,(0,0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground,(ground_scroll,650))
    ground_scroll=ground_scroll-4
    if abs(ground_scroll)>35:
        ground_scroll=0
        
    
    

    
    

    pygame.display.update()

