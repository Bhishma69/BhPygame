import random
import math
import pygame

# innitialize pygame(
pygame.init()

# create pygame window
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("milk.jpg")
# Title and icon
pygame.display.set_caption("SPACE WAR")
icon = pygame.image.load("project.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.jpg"))
    enemyX.append(random.randint(0, 735))
    enemyX_change.append(4)
    enemyY_change.append(40)
    enemyY.append(random.randint(50, 150))

# Bullet

# ready -state means u cant see the bullet on the screen
# fire- the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletX_change = 0
bulletY_change = 10
bulletY = 480
bullet_state = "ready"


#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
testY=10

def show_score(x,y):
    score=font.render("Score :" +str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))




def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletY, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    # RGB - red,green ,blue
    screen.fill((42, 42, 42))
    # Background IMage
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether left or right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change -= 5

            if event.key == pygame.K_RIGHT:
                playerX_change += 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # gets the current x coordinate of the spaceship

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    player(playerX, playerY)

    # checking for boundaries of spaceship so that it doesnt goes out of window
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy movement
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:

            enemyX_change[i] = -3.5
            enemyY[i] += enemyY_change[i]
        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    show_score(textX,testY)

    pygame.display.update()
