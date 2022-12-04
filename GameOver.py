import arcade
# class used to end game / game over
class GameOverView(arcade.View):
# initialization and an attempt to initialize a png
    def __init__(self):
        super().__init__()
        self.game_over = arcade.load_texture("GameOver.png")
        arcade.set_viewport(0, 1200 - 1, 0, 700 - 1)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.game_over.draw()
        arcade.finish_render()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)