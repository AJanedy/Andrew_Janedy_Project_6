from GameOver import GameOverView
import arcade
import random
# class creation for main call
class GameView(arcade.View):
# initialization of class attributes
    def __init__(self):
        super().__init__()
        self.player = None
        self.player_dx = 0
        self.enemy1 = arcade.SpriteList()
        self.score = 0
        self.fire_sound = None
        self.hit_sound = None
        self.death_sound = None
        self.fire = arcade.SpriteList()
        self.enemy_count = 6
# setup function / assigns sprite and starting location to self.player
    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/robot/robot_climb0.png")
        self.player.center_x = 600
        self.player.center_y = 65
    def on_draw(self):
# begins render / draws player/laser/zombie
        arcade.start_render()
        self.player.draw()
        self.fire.draw()
        self.enemy1.draw()
# score display
        my_text = arcade.Text(f"Score: {self.score}", 1080, 25, arcade.color.WHITE, 20)
        my_text.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
# if statement that continues to add an enemy so that 6 are always on screen
        if len(self.enemy1) < self.enemy_count:
            enemy = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png")
            enemy.center_x = random.randint(36, 1164)
            enemy.center_y = 774
            self.enemy1.append(enemy)
# allows for wall pass through
        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 0
        if self.player.center_x < 0:
            self.player.center_x = 1200
# moves laser upward
        for sprite in self.fire:
            if sprite.center_y < 800:
                sprite.center_y += 10
# moves zombies downward
        for sprite in self.enemy1:
            if sprite.center_y > -74:
                sprite.center_y -= 1
# collision detection, zombie removal, score update
        for sprite in self.fire:
            shot_zombies = arcade.check_for_collision_with_list(sprite, self.enemy1)
            if sprite.center_y >= 750:
                self.fire.remove(sprite)
            for extra_dead_zombies in shot_zombies:
                self.hit_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
                arcade.play_sound(self.hit_sound)
                self.score += 1
                self.enemy1.remove(extra_dead_zombies)
                if sprite in self.fire:
                    self.fire.remove(sprite)
                enemy = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png")
                enemy.center_x = random.randint(36, 1164)
                enemy.center_y = 774
                self.enemy1.append(enemy)
# FIXME: game over collision detection and game over screen
        zombified_robot = arcade.check_for_collision_with_list(self.player, self.enemy1)
        if zombified_robot:
            self.death_sound = arcade.load_sound(":resources:sounds/gameover1.wav")
            arcade.play_sound(self.death_sound)
            #self.game_over = True
            view = GameOverView()
            self.window.show_view(view)
# game over for sprite past bottom of screen
        for sprite in self.enemy1:
            if sprite.center_y < 74:
                self.death_sound = arcade.load_sound(":resources:sounds/gameover1.wav")
                arcade.play_sound(self.death_sound)
                #self.game_over = True
                view = GameOverView()
                self.window.show_view(view)
# mouse movement
    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
# mouse click fire
    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.fire) < 5:
            self.fire_sound = arcade.load_sound(":resources:sounds/laser1.wav")
            arcade.play_sound(self.fire_sound)
            fire = arcade.Sprite(":resources:images/space_shooter/laserRed01.png")
            fire.center_x = self.player.center_x
            fire.center_y = self.player.center_y + 74
            self.fire.append(fire)
#left / right movement and space fire
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -5
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 5
        if symbol == arcade.key.SPACE:
            if len(self.fire) < 5:
                self.fire_sound = arcade.load_sound(":resources:sounds/laser1.wav")
                arcade.play_sound(self.fire_sound)
                fire = arcade.Sprite(":resources:images/space_shooter/laserRed01.png")
                fire.center_x = self.player.center_x
                fire.center_y = self.player.center_y + 74
                self.fire.append(fire)
# stops left and right movement upon key release
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_dx = 0

if __name__ == "__main__":
    import GameDriver
    GameDriver.main()
