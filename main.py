import pygame
from pygame.locals import *
import random
pygame.init()
Turn = 0
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Recycling Project")
red = 255, 0, 0
flag = True
def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
x = 250
y = 400
x1 = 50
y1 = 50
flag1 = False
Bin = pygame.image.load("9521209302025559564.png")
Bin = pygame.transform.scale(Bin,(100,100))
Soda = pygame.image.load("Soda.png")
Soda = pygame.transform.scale(Soda,(50,100))
Peel = pygame.image.load("Banana peel.png")
Peel = pygame.transform.scale(Peel,(70,100))
Paper = pygame.image.load("Paper.png")
Paper = pygame.transform.scale(Paper,(70,80))
points = 0
type = random.randint(1, 2)
flag2 = None
while True:
    screen.fill((255, 255, 255))
    if flag2 == True:
        show_text("Help", 195, 20, red)
        show_text("- Move around the bin using the arrow keys", 5, 100, red)
        show_text("- Catch the recyclables, like the soda can,", 5, 150, red)
        show_text(" paper and the cardboard box ", 5, 180, red)
        show_text("- Don't catch the non - recyclables,", 5, 230, red)
        show_text(" like the banana peel  ", 5, 260, red)
        show_text("- If you catch a recyclable, you get +1 points,", 5, 300, red)
        show_text(" and if you catch a non - recyclable it is - 1  ", 5, 330, red)
        show_text("- If you do not catch a recyclable the game", 5, 360, red)
        show_text(" is over. But if you leave the banana peel, + 1", 5, 390, red)
    if flag == True:
        pygame.draw.rect(screen, (0, 0, 255), (150, 150, 200, 50))
        show_text("Play", 220, 165, red)
        pygame.draw.rect(screen, (0, 0, 255), (150, 300, 200, 50))
        show_text("Help", 220, 315, red)
    if flag == False:
        points = str(points)
        show_text(points, 50, 50, red)
        screen.blit(Bin, (x, y))
        if flag1 == True:
            if type == 1:
                screen.blit(Soda, (x1, y1))
            if type == 2:
                screen.blit(Peel, (x1, y1))
            if type == 3:
                screen.blit(Paper, (x1, y1))
        y1 = y1 + 2
        if y1 + 60 in range(400, 500) and x1 in range(x,x+50):
            if type == 3:
                print("Paper")
                points = int(points)
                points = points + 1
                points = str(points)
            if type == 2:
                if points == 0:
                    print("Game over")
                    break
                else:
                    points = int(points)
                    points = points - 1
                    points = str(points)
                print("Peel")
                show_text(points, 100, 50, red)
            if type == 1:
                print("Soda")
                points = int(points)
                points = points + 1
                points = str(points)
            print(points)
            flag1 = False
            x1 = random.randint(0,470)
            y1 = random.randint(-30,30)
            type = random.randint(1, 3)
            screen.blit(Bin, (x, y))
            flag1 = True
    if y1 == 500:
        if type == 2:
            flag1 = True
            x1 = random.randint(0, 470)
            y1 = random.randint(-30, 30)
            points = int(points)
            points = points + 1
            points = str(points)
        else:
            print("Game over")
            break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] in range(150, 350) and event.pos[1] in range(150, 200):
                pass
                screen.fill((255, 255, 255))
                flag = False
                flag1 = True
            if event.pos[0] in range(150, 350) and event.pos[1] in range(300, 450):
                print("Found")
                screen.fill((255, 255, 255))
                flag2 = True
                flag1 = None
                flag = None
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_LEFT:
                x = x - 20
    pygame.display.update()
