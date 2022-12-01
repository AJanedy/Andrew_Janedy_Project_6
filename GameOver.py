import arcade

class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("GameOver.png")

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(600, 350, 1200, 700)


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)