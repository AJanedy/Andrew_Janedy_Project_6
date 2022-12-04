import arcade
class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
        self.game_over = arcade.load_texture("GameOver.png")
        arcade.set_viewport(0, 1200 - 1, 0, 700 - 1)

    def on_draw(self):
        self.clear()
        #arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                 #        arcade.color.WHITE, font_size=50, anchor_x="center")
        #self.game_over.draw_sized(1200 / 2, 700 / 2,
                              #  1200, 700)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)