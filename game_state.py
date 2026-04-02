from enum import Enum


class GameSystem(Enum):
    ROUND_DONE = 1
    GAME_OVER = 2
    NOT_STARTED = 3
    ROUND_ACTIVE = 4
