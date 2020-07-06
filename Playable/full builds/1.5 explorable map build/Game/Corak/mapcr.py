import pygame
from Game.Corak.dicio import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, name, size, andar1, sala1):
        pygame.sprite.Sprite.__init__(self)
        size = int(size / 2)
        andar1 = int(andar1 / 2)
        sala1 = int(sala1 / 2)
        self.type = 0
        self.image = pygame.Surface([size, size])
        self.image.fill(BLACK)
        self.at = [sala1, andar1]
        self.rect = self.image.get_rect()
        self.rect.x = self.at[0]
        self.rect.y = self.at[1]
        #alltiles.append(self)

        if "room" in name: self.image.fill(BLUE)
        if "_hall" in name: self.image.fill(RED)
        if "_strt" in name: self.image.fill(YELLOW)
        if "_key" in name: self.image.fill(RED)
        if "mod" in name: self.image.fill(GRAY)
        if "_entr" in name: self.image.fill(GREEN)
        if "_end" in name: self.image.fill(YELLOW)
        if "-strt" in name: self.image.fill([GRAY[0] + 50, GRAY[1], GRAY[2]])
        if "-key1" in name: self.image.fill([GRAY[0] + 100, GRAY[1], GRAY[2]])
        if "-key2" in name: self.image.fill([GRAY[0] + 100, GRAY[1], GRAY[2] + 50])
        if "-end" in name: self.image.fill([GRAY[0] + 100, GRAY[1]-50, GRAY[2] + 100])


def printmap(level):
    #alltiles = []
    map = pygame.sprite.Group()
    #while len(alltiles) > 0: del alltiles[0]
    for andar in range(len(level)):
        for sala in range(len(level[andar])):
            if "UDcorridor" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27)]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27 + (9 * 2))]
                    map.add(tile)
            if "LRcorridor" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
            if "LDturn" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + 9, sala * 27 + (9 * 2))
                map.add(tile)
                tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27), Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))]
                map.add(tile)
            if "RDturn" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + 9, sala * 27)
                map.add(tile)
                tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27), Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))]
                map.add(tile)
            if "RUturn" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27)]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * 2))
                map.add(tile)
                for temp in range(1, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
            if "LUturn" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27 + (9 * 2))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27)
                map.add(tile)
                for temp in range(0, 2):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
            if "Uroom" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27 + (9 * 2))]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27)]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + 9)
                map.add(tile)
            if "Droom" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27 + (9 * 2))]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27)]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27 + 9)
                map.add(tile)
            if "Rroom" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + 9, sala * 27)
                map.add(tile)
            if "Lroom" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + 9, sala * 27 + (9 * 2))
                map.add(tile)
            if "hall" in level[andar][sala]:
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27)
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * 2))
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27)
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))
                map.add(tile)
            if "LUD3" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27 + (9 * 2))]
                    map.add(tile)
                    tile = Tile(level[andar][sala], 9, andar * 27, sala * 27)
                    map.add(tile)
                    tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27)
                    map.add(tile)
            if "RUD3" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp), sala * 27)]
                    map.add(tile)
                    tile = Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * 2))
                    map.add(tile)
                    tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))
                    map.add(tile)
            if "LRD3" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27)
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))
                map.add(tile)
            if "LRU3" in level[andar][sala]:
                for temp in range(0, 3):
                    tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * temp))]
                    map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27 + (9 * 2))
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27 + (9 * 2), sala * 27 + (9 * 2))
                map.add(tile)
                tile = Tile(level[andar][sala], 9, andar * 27, sala * 27)
                map.add(tile)
            if "Blank" in level[andar][sala]:
                for temp in range(0, 3):
                    for temp2 in range(0, 3):
                        tile = [Tile(level[andar][sala], 9, andar * 27 + (9 * temp2), sala * 27 + (9 * temp))]
                        map.add(tile)

    return map
'''
screen = pygame.display.set_mode((ScreenX, ScreenY))
mapgen = True
x, y = 0, 0
clock = pygame.time.Clock()
temp = 0
tiles = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mapgen = True if not mapgen else False

            if event.key == pygame.K_a:
                tiles = printmap(tiles)
    mousex, mousey = pygame.mouse.get_pos()

    pygame.display.set_caption(str(round(clock.get_fps())))
    clock.tick(FPS)
    screen.fill(WHITE)
    if not mapgen:
        tiles = printmap(tiles)
    pygame.draw.rect(screen, RED, [mousex, mousey, temp, 5])
    tiles.draw(screen)
    #pygame.draw.rect(screen, BLACK, [int(b), c, 10, 10])
    pygame.display.flip()

pygame.quit()
'''