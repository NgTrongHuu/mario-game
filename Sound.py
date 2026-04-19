import pygame as pg


class Sound(object):
    def __init__(self):
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        self.sounds['overworld'] = pg.mixer.Sound('mario/Next/sounds/overworld.wav')
        self.sounds['overworld_fast'] = pg.mixer.Sound('mario/Next/sounds/overworld-fast.wav')
        self.sounds['level_end'] = pg.mixer.Sound('mario/Next/sounds/levelend.wav')
        self.sounds['coin'] = pg.mixer.Sound('mario/Next/sounds/coin.wav')
        self.sounds['small_mario_jump'] = pg.mixer.Sound('mario/Next/sounds/jump.wav')
        self.sounds['big_mario_jump'] = pg.mixer.Sound('mario/Next/sounds/jumpbig.wav')
        self.sounds['brick_break'] = pg.mixer.Sound('mario/Next/sounds/blockbreak.wav')
        self.sounds['block_hit'] = pg.mixer.Sound('mario/Next/sounds/blockhit.wav')
        self.sounds['mushroom_appear'] = pg.mixer.Sound('mario/Next/sounds/mushroomappear.wav')
        self.sounds['mushroom_eat'] = pg.mixer.Sound('mario/Next/sounds/mushroomeat.wav')
        self.sounds['death'] = pg.mixer.Sound('mario/Next/sounds/death.wav')
        self.sounds['pipe'] = pg.mixer.Sound('mario/Next/sounds/pipe.wav')
        self.sounds['kill_mob'] = pg.mixer.Sound('mario/Next/sounds/kill_mob.wav')
        self.sounds['game_over'] = pg.mixer.Sound('mario/Next/sounds/gameover.wav')
        self.sounds['scorering'] = pg.mixer.Sound('mario/Next/sounds/scorering.wav')
        self.sounds['fireball'] = pg.mixer.Sound('mario/Next/sounds/fireball.wav')
        self.sounds['shot'] = pg.mixer.Sound('mario/Next/sounds/shot.wav')

    def play(self, name, loops, volume):
        self.sounds[name].play(loops=loops)
        self.sounds[name].set_volume(volume)

    def stop(self, name):
        self.sounds[name].stop()

    def start_fast_music(self, core):
        if core.get_map().get_name() == '1-1':
            self.stop('overworld')
            self.play('overworld_fast', 99999, 0.5)