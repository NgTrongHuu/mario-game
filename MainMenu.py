import pygame as pg

from Const import *
from Text import Text


class MainMenu(object):
    def __init__(self):
        self.background = pg.image.load(r'mario/Next/images/loading_background.png').convert()
    def render(self, core):
        core.screen.blit(self.background, (0, 0))
