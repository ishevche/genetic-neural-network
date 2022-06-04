import numpy as np

EYES_AMOUNT = 24
INPUT_LAYER = 2 * EYES_AMOUNT + 3
HIDDEN_LAYER = 24
OUTPUT_LAYER = 2
MAX_X_COORD = 99
MAX_Y_COORD = 99
RADIUS = 1
BASE_ENERGY = 100
BASE_ENERGY_RECEIVE = 1
FLOWER_ENERGY_SCALE = 0.1
MAX_ANGULAR_VELOCITY = np.pi / 90
BASE_CONSUMPTION = 1
MOVEMENT_CONSUMPTION = 1
FLOWERS_AMOUNT = 200
POPULATION_SIZE = 300
VIEW_DISTANCE = 5.0
MUTATION_PERCENT = 10
MAX_VIEW_ANGLE = 3 * np.pi / 4
MIN_VIEW_ANGLE = np.pi / 12
