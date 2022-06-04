import datetime

import numpy
from manimlib import *

sys.path.append('/home/ivan/Documents/UCU/DM_2021/Project2')
import constants
from generation import Generation
from organism import Flower


class MyScene(Scene):

    def construct(self):
        self.camera.frame.set_height(105).move_to(UR * 50)
        self.add(Square(101).move_to(UR * 49.5))
        self.animations = [list()]
        sim = Generation(self)
        random.seed(round(time.time() * 1000) % (2 ** 32 - 1))
        numpy.random.seed(round(time.time() * 1000) % (2 ** 32 - 1))
        sim.set_random_population(constants.POPULATION_SIZE)
        sim.run()
        print('ready')

    def next_move_setup(self):
        self.animations.append(list())

    @staticmethod
    def new_organism(organism, size):
        if isinstance(organism, Flower):
            return Circle(radius=0.5, color=GREEN, fill_opacity=1) \
                .move_to(RIGHT * organism.coordinates[0] +
                         UP * organism.coordinates[1])
        else:
            return Circle(radius=size, color=RED,
                          fill_opacity=organism.size * 0.5 + 0.5) \
                .move_to(RIGHT * organism.coordinates[0] +
                         UP * organism.coordinates[1])
