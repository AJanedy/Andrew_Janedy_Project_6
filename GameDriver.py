import arcade
from main import GameView

def main():
    window = arcade.Window(1200, 700, "Arcade Class Window Demo")
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()

main()