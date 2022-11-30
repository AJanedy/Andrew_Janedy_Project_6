import arcade
from main import GameWindow

def main():
    gameWindow = GameWindow()
    arcade.set_background_color(arcade.color.BLACK)
    gameWindow.setup()
    arcade.run()

main()