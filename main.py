import arcade
import random
from game_state import GameSystem
from attack_animation import AttackAnimation, AttackType

"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Rock,Paper,Scissors!"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.GRAY

        self.sprites = arcade.SpriteList()
        jouer = arcade.Sprite("assets/faceBeard.png", scale=0.5)
        jouer.position = (400, 400)
        computer = arcade.Sprite("assets/compy.png", scale=2.5)
        computer.position = (880, 400)
        self.sprites.append(jouer)
        self.sprites.append(computer)

        self.rock_list = arcade.SpriteList()
        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.position = (250, 200)
        self.rock_list.append(self.rock)

        self.paper_list = arcade.SpriteList()
        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.position = (400, 200)
        self.paper_list.append(self.paper)

        self.scissors_list = arcade.SpriteList()
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors.position = (550, 200)
        self.scissors_list.append(self.scissors)

        self.gamestate = GameSystem(1)
        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes need to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.sprites.draw()
        self.rock_list.draw()
        self.paper_list.draw()
        self.scissors_list.draw()
        arcade.draw_lrbt_rectangle_outline(200, 300, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(350, 450, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(500, 600, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(830, 930, 150, 250, arcade.color.YELLOW)
        title = arcade.Text("ROCHE PAPIER CISEAUX", 340, 600, arcade.color.BLACK, font_size=45)
        title.draw()
        points = arcade.Text("Pointage de Jouer:", 100, 100, arcade.color.DARK_BLUE, font_size=20)
        points.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.rock.on_update()
        self.paper.on_update()
        self.scissors.on_update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.SPACE:
            self.gamestate = 2

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
