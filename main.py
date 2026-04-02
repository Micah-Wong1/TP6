import arcade
import random
from game_state import GameSystem

screen_width = 640
screen_height = 480
window_title = "Arcade?"


def main():
    arcade.open_window(screen_width, screen_height, window_title)
    arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)

    arcade.start_render()

    arcade.finish_render()
    arcade.run()


main()

