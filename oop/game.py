import pygame

pygame.init()
win=pygame.display.set_mode((500, 500))#создали окно
pygame.display.set_caption("Igra Dimona")#название игры

walkRight = [pygame.image.load('Game/right_1.png'), pygame.image.load('Game/right_2.png'),
             pygame.image.load('Game/right_3.png'), pygame.image.load('Game/right_4.png'),
             pygame.image.load('Game/right_5.png'), pygame.image.load('Game/right_6.png')]
walkLeft = [pygame.image.load('Game/left_1.png'), pygame.image.load('Game/left_2.png'),
            pygame.image.load('Game/left_3.png'), pygame.image.load('Game/left_4.png'),
            pygame.image.load('Game/left_5.png'), pygame.image.load('Game/left_6.png')]
bg = pygame.image.load('Game/bgg.jpg')
playerStand = pygame.image.load('Game/idle.png')

clock = pygame.time.Clock()
#характеристики персонажа
x = 50
y = 425
width = 60
height = 71
#так как изображение персонажа в формате 60x71
speed = 5

isJumping = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1>= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()

run = True
while run:
    clock.tick(30)#30 фреймов в секунду

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #начало координат в левом верхнем углу
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500-width-5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0

    if not(isJumping):
        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount) ** 2 / 2
            else:
                y -= (jumpCount) ** 2 / 2
            jumpCount -= 1
        else:
            isJumping = False
            jumpCount = 10
    drawWindow()

pygame.quit()


            #if keys[pygame.K_DOWN] and y<500-height-15:
                #y += speed
            #if keys[pygame.K_UP] and y>5:
                #y -= speed
