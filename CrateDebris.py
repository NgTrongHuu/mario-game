import pygame as pg


class CrateDebris(object):
    """
    
    Text that appears when player collects a crate.
    Shows how many crates collected.
    
    """
    def __init__(self, x_pos, y_pos, crate_count):
        self.font = pg.font.Font('mario/Next/fonts/emulogic.ttf', 16)
        self.text = self.font.render('+' + str(crate_count), False, (255, 255, 255))
        self.rect = self.text.get_rect(center=(x_pos, y_pos))
        self.y_offset = 0

    def update(self, core):
        """
        Move text upward and remove after animation
        """
        self.rect.y -= 1
        self.y_offset -= 1

        if self.y_offset == -100:
            core.get_map().crate_debris.remove(self)

    def render(self, core):
        """
        Render in game world with camera offset
        """
        core.screen.blit(self.text, core.get_map().get_camera().apply(self))
