import pygame

# region CLASSES
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > _SCREEN_WIDTH:
            self.rect.right = _SCREEN_WIDTH
    def shoot(self):
        x = self.rect.centerx
        y = self.rect.top
        b = Bullet("bullet.png", x, y, 16, 20, speed = 6)
        b.rect.centerx = x
        bullets.add(b)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > _SCREEN_HEIGHT: 
            self.rect.x = randint(0, _SCREEN_WIDTH - self.rect.width)
            self.rect.bottom = 0
 
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0: 
            self.kill()

class TextSprite(sprite.Sprite):
    def __init__(self, text, size, color_text, position):
        super().__init__()
        self.text = text
        self.position = position
        self.color = color_text
        self.local_font = font.Font(None, size)
        self.image = self.local_font.render(self.text, True, color_text)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    def update(self, new_text):
        self.text = new_text
        self.image = self.local_font.render(self.text, True, self.color)

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > _SCREEN_HEIGHT: 
            self.rect.x = randint(0, _SCREEN_WIDTH - self.rect.width)
            self.rect.bottom = 0

# endregion CLASSES
