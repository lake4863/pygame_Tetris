import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

brick_length = 20
shape_I = {0:0, brick_length:0, brick_length*2:0, brick_length*3:0}

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('A Tetris!')

clock = pygame.time.Clock()

brickImg = pygame.image.load('brick.jpg')

def brick(x, y):
    gameDisplay.blit(brickImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    # while go_on != 'Y' or go_on != 'y':
    #     time.sleep(2)

    #     prompt = 'Do you want to start a new game? (Y=yes)'
    #     go_on = input(prompt)

    #     game_loop()

#def touched_bottom():

#def touched_side():

def touched_top():
    message_display('Game Over!')

def game_loop():
    x = 600
    y = 400

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # move left
                    x_change = -brick_length
                elif event.key == pygame.K_RIGHT:
                    # move right
                    x_change = brick_length
                elif event.key == pygame.K_DOWN:
                    # move down
                    y_change = brick_length
                elif event.key == pygame.K_UP:
                    # rotate 90 degrees
                    rotate()

            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_:
                    #clock.tick(0)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    
        x += x_change
        y += y_change

        gameDisplay.fill(white)
        brick(x, y)

        if x > display_width - brick_length or x < 0:
            touched_side() # in new loop still move the brick
        if y > display_height - brick_length or y < 0:
            touched_bottom()

        pygame.display.update()
        
        speed = 5
        clock.tick(speed)

game_loop()
pygame.quit()
quit()
