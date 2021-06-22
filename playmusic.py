import pygame


def PlayWavFie(Filename = "./delete.mp3"):
    pygame.init()
    pygame.mixer.music.load(Filename)
    pygame.mixer.music.play(1)