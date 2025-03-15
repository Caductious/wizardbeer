import pygame

WIDTH_SCREEN = 1000
WIDTH = 800
HEIGHT = 800
FPS = 60

bg = pygame.image.load('resources/images/field.png')
player = [pygame.image.load('resources/images/player.png'), pygame.image.load('resources/images/player2.png')]
gnome = [pygame.image.load('resources/images/gnome.png'), pygame.image.load('resources/images/gnome2.png')]
beer = pygame.image.load('resources/images/beer.png')

pygame.font.init()
font = pygame.font.Font('resources/fonts/Vezitsa.ttf', 60)

with open('high_score.txt', 'r') as file:
    hs = file.readline()
    high_score = font.render(hs, True, 'Yellow')

music_path = 'resources/audio/gnome_music.mp3'
laugh_path = 'resources/audio/hihi.mp3'