import pygame as pg
import sys

"""This is the More information module which
will provide more information about the game
foundation and the game style. """

width = 600
height = 400

gameDisplay = pg.display.set_mode((width, height))
pg.display.set_caption('More Information')

white = (255, 255, 255) #RGB

textMessage1 = pg.image.load('Text1.png')

def text(x, y):
    gameDisplay.blit(textMessage1, (x, y))

x = (width * 0.2)
y = (height * 0.1)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    gameDisplay.fill(white)
    text(x, y)
 
    pg.display.update()

pg.quit()
quit()
