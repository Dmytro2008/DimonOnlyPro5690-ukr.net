import pygame

pygame.init()
win=pygame.display.set_mode((500, 500))#создали окно
pygame.display.set_caption("Igra Dimona")#название игры

#характеристики персонажа
x = 50
y = 425
width = 40
height = 60
speed = 5

isJumping = False
jumpCount = 10
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #начало координат в левом верхнем углу
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500-width-5:
        x += speed
    if not(isJumping):
            if keys[pygame.K_DOWN] and y<500-height-15:
                y += speed
            if keys[pygame.K_UP] and y>5:
                y -= speed
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

    win.fill((0, 0, 0))


    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
