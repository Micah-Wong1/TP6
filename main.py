import arcade
import random
from game_state import GameSystem
from attack_animation import AttackAnimation, AttackType

"""
Nom: Micah
Gr: 406
Ce code cree un jeu de roche, papier, scissaux contre un AI.
"""

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Rock,Paper,Scissors!"


class GameView(arcade.View):

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

        self.paper_list = arcade.SpriteList()
        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.position = (400, 200)

        self.scissors_list = arcade.SpriteList()
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors.position = (550, 200)

        self.rock_list.append(self.rock)
        self.paper_list.append(self.paper)
        self.scissors_list.append(self.scissors)

        self.player_attack_type = None
        self.computer_attack_type = None

        self.player_score = 0
        self.computer_score = 0

        self.game_state = GameSystem.NOT_STARTED

    def on_draw(self):
        """
        Afficher l'écran
        """

        self.clear()
        self.sprites.draw()

        arcade.draw_lrbt_rectangle_outline(200, 300, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(350, 450, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(500, 600, 150, 250, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_outline(830, 930, 150, 250, arcade.color.YELLOW)

        title = arcade.Text("ROCHE PAPIER CISEAUX", 350, 600, arcade.color.BLACK, font_size=45)
        title.draw()

        player_points = arcade.Text(f"Pointage de Jouer: {self.player_score}", 100, 100,
                                    arcade.color.DARK_BLUE, font_size=20)
        player_points.draw()

        comp_points = arcade.Text(f"Pointage de Ordinateur: {self.computer_score}", 700, 100,
                                  arcade.color.DARK_BLUE, font_size=20)
        comp_points.draw()

        if self.game_state == GameSystem.NOT_STARTED:
            instructions = arcade.Text("PRESS SPACE TO START", 400, 500, arcade.color.BLACK, font_size=35)
            instructions.draw()
        elif self.game_state == GameSystem.ROUND_ACTIVE:
            instructions = arcade.Text("PLAY!", 600, 500, arcade.color.BLACK, font_size=35)
            instructions.draw()
            self.rock.position = (250, 200)
            self.rock_list.draw()

            self.paper.position = (400, 200)
            self.paper_list.draw()

            self.scissors.position = (550, 200)
            self.scissors_list.draw()
        elif self.game_state == GameSystem.GAME_OVER:
            if self.player_score < self.computer_score:
                outcome = arcade.Text("VOUS PERDEZ...", 550, 400, arcade.color.DARK_RED, font_size=20)
                outcome.draw()
            elif self.player_score > self.computer_score:
                outcome = arcade.Text("VOUS GAGNEZ!!!", 550, 400, arcade.color.DARK_RED, font_size=20)
                outcome.draw()
            instructions = arcade.Text("APPUYEZ SUR ESPACE POUR RECOMMENCER", 280, 500, arcade.color.BLACK,
                                       font_size=35)
            instructions.draw()
        elif self.game_state == GameSystem.ROUND_DONE:
            instructions = arcade.Text("APPUYEZ SUR ESPACE POUR CONTINUER", 280, 500, arcade.color.BLACK,
                                       font_size=35)
            instructions.draw()
            if self.player_attack_type == self.computer_attack_type:
                drawchoice = arcade.Text("Match Nul!", 570, 400, arcade.color.DARK_BLUE, font_size=20)
                drawchoice.draw()
            elif (self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS or
                    self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK or
                    self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER):
                roundwin = arcade.Text("Match Gagné!", 570, 400, arcade.color.DARK_BLUE, font_size=20)
                roundwin.draw()
            elif (self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER or
                  self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS or
                  self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK):
                roundlost = arcade.Text("Match Perdu!", 570, 400, arcade.color.DARK_BLUE, font_size=20)
                roundlost.draw()

            if self.player_attack_type == AttackType.ROCK:
                self.rock.position = (250, 200)
                self.rock_list.draw()

            if self.player_attack_type == AttackType.PAPER:
                self.paper.position = (400, 200)
                self.paper_list.draw()

            if self.player_attack_type == AttackType.SCISSORS:
                self.scissors.position = (550, 200)
                self.scissors_list.draw()

            if self.computer_attack_type == AttackType.ROCK:
                self.rock.position = (880, 200)
                self.rock_list.draw()
            if self.computer_attack_type == AttackType.PAPER:
                self.paper.position = (880, 200)
                self.paper_list.draw()
            if self.computer_attack_type == AttackType.SCISSORS:
                self.scissors.position = (880, 200)
                self.scissors_list.draw()

    def on_update(self, delta_time):
        """
        garantit la logique du jeu
        """
        self.rock.on_update()
        self.paper.on_update()
        self.scissors.on_update()

        if self.game_state != GameSystem.ROUND_ACTIVE:
            return

        if self.player_attack_type is None:
            return

        pc_attack = random.randint(0, 2)
        if pc_attack == 0:
            self.computer_attack_type = AttackType.ROCK
        elif pc_attack == 1:
            self.computer_attack_type = AttackType.PAPER
        else:
            self.computer_attack_type = AttackType.SCISSORS

        if self.player_attack_type == self.computer_attack_type:
            pass
        elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER:
            self.computer_score += 1
        elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
            self.player_score += 1
        elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
            self.player_score += 1
        elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS:
            self.computer_score += 1
        elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
            self.computer_score += 1
        elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
            self.player_score += 1

        self.game_state = GameSystem.ROUND_DONE

        if self.player_score == 3 or self.computer_score == 3:
            self.game_state = GameSystem.GAME_OVER

    def on_key_press(self, key, key_modifiers):
        """
        modifie l'état du jeu via la touche espace
        """

        if key == arcade.key.SPACE:
            if self.game_state == GameSystem.NOT_STARTED:
                self.game_state = GameSystem.ROUND_ACTIVE

            elif self.game_state == GameSystem.ROUND_DONE:
                self.game_state = GameSystem.ROUND_ACTIVE
                self.player_attack_type = None

            elif self.game_state == GameSystem.GAME_OVER:
                self.game_state = GameSystem.ROUND_ACTIVE
                self.player_score = 0
                self.computer_score = 0
                self.player_attack_type = None
                self.computer_attack_type = None

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        permet de choisir une attaque
        """
        if self.game_state != GameSystem.ROUND_ACTIVE:
            return

        if self.rock.collides_with_point((x, y)):
            self.player_attack_type = AttackType.ROCK

        elif self.paper.collides_with_point((x, y)):
            self.player_attack_type = AttackType.PAPER

        elif self.scissors.collides_with_point((x, y)):
            self.player_attack_type = AttackType.SCISSORS


def main():
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
