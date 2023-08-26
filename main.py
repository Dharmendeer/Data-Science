import pygame, sys

pygame.init()

width=600
hieght=600
line_width=15

red= (255, 0, 0)
BG_COLOR =(28, 170, 156)
line_color=(23, 145, 135)

screen = pygame.display.set_mode((width, hieght))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOR)

#pygame.draw.line(screen, BG_COLOR, (10,10), (300, 300), 10)

def draw_lines():
    pygame.draw.line( screen, line_color, (0,200), (600, 200), line_width)

draw_lines()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update