import pygame as pg


class Crate(object):
    """
    
    Crate/Chest object that Mario can collect.
    
    """
    def __init__(self, x_pos, y_pos):
        self.rect = pg.Rect(x_pos, y_pos, 32, 32)
        self.image = pg.image.load('mario/Next/images/crate.png').convert_alpha()
        self.type = 'Crate'
        
        self.collected = False
        self.collection_tick = 0
        self.blink_speed = 5  # Speed of blinking effect

    def update(self, core):
        """
        Update crate animation when collected
        """
        if self.collected:
            self.collection_tick += 1
            # Remove after blinking animation (50 ticks = about 1 second at 50 FPS)
            if self.collection_tick >= 50:
                core.get_map().crates.remove(self)

    def collect(self, core):
        """
        Collect the crate
        """
        if not self.collected:
            self.collected = True
            self.collection_tick = 0
            core.get_map().get_player().add_crates(1)
            core.get_map().spawn_crate_text(self.rect.x, self.rect.y - 32, crate_count=1)
            core.get_sound().play('coin', 0, 0.5)

    def render(self, core):
        # Blinking effect when collected
        if self.collected:
            # Blink: visible for first 25 ticks, invisible for next 25 ticks
            if (self.collection_tick // self.blink_speed) % 2 == 0:
                core.screen.blit(self.image, core.get_map().get_camera().apply(self))
        else:
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))
