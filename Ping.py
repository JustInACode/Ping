# region SETUP
# import modules
from telnetlib import GA
from pygame import *
from random import randint
# create the window and the clock
_SCREEN_WIDTH = 1024    
_SCREEN_HEIGHT = 720
window = display.set_mode((_SCREEN_WIDTH, _SCREEN_HEIGHT))
clock = time.Clock()
font.init()
# endregion SETUP

class GameSprite(sprite.Sprite):
    def __init__(self, imagefile, x, y, width, height, speed=0):
        sprite.Sprite.__init__(self)
        self.image = image.load(imagefile)
        self.image = transform.scale(self.image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, imagefile, x, y, width, height, key_up, key_down, speed=0):
        super().__init__(imagefile, x, y, width, height, speed)
        self.key_up = key_up
        self.key_down = key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > _SCREEN_HEIGHT:
            self.rect.bottom = _SCREEN_HEIGHT

class Ball(GameSprite):
    def update(self):
        if self.rect.bottom >= _SCREEN_HEIGHT or self.rect.top < 0:
            self.speed.y *= -1
        self.rect.topleft += self.speed
        

ball = Ball("ball.jpg", 400, 300, 50, 50, speed=Vector2(6, 4))

paddle_left = Player(imagefile="Paddle1.png", x=20, y=280, width=20, height=120, 
                    key_up=K_w, key_down=K_s, speed=10)
paddle_right = Player(imagefile="Paddle2.png", x=_SCREEN_WIDTH-40, y=280, width=20, height=120, 
                    key_up=K_UP, key_down=K_DOWN, speed=10)

r_p_win = font.Font(None, 100).render("Right player wins!", True, 'crimson')
l_p_win = font.Font(None, 100).render("Left player wins!", True, 'crimson')

while not event.peek(QUIT):
    if ball.rect.left < 0:
        window.blit(r_p_win, (225,320))
    elif ball.rect.right > _SCREEN_WIDTH:
        window.blit(l_p_win, (225,320))
    else:
        
        window.fill('lightblue')

        if sprite.collide_rect(ball, paddle_left) or sprite.collide_rect(ball, paddle_right):
            ball.speed.x *= -1

        ball.update()
        ball.draw(window)
        paddle_left.update()
        paddle_left.draw(window)
        paddle_right.update()
        paddle_right.draw(window)


    display.update()
    clock.tick(60)