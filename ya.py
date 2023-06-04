from random import randint
from pygame import *
init()



win_width = 1280
win_heigh = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_a_d(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heigh - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
            GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
            self.side = side
    def update(self):
        global side
        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed
window = display.set_mode((win_width, win_heigh))
display.set_caption('Rakada')
dackground = transform.scale(image.load('images/bgr.png'), (win_widthm win_heigh))





game = True
finish = False
clock = time.Clock()
FPS = 100


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        iteems.draw(window)
        packman.update_l_r()
        packman.update_a_d()
        for monster in monsters:
            monster.update()
    coin_c = font2.render('coins:' + str(c_count), True,(246,249,128))
    window.blit(coin_c, (40, 0))
    display.update()
    clock.tick(FPS)
