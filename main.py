import arcade
import random

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(1200, 700, "Arcade Class Window Demo")
        self.player = None
        self.player_dx = 0
        self.enemy1 = arcade.SpriteList()
        self.score = 0
        self.sound1 = None
        self.sound2 = None
        self.sound3 = None
        self.fire = arcade.SpriteList()


    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/robot/robot_climb0.png")
        self.player.center_x = 600
        self.player.center_y = 65

        for number in range(3):
            enemy = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png")
            enemy.center_x = random.randint(36, 1164)
            enemy.center_y = 664
            self.enemy1.append(enemy)

    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.fire.draw()
        self.enemy1.draw()

        arcade.finish_render()

    def on_update(self, delta_time):

        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 0
        if self.player.center_x < 0:
            self.player.center_x = 1200

        for sprite in self.fire:
            if sprite.center_y < 800:
                sprite.center_y += 10

        for sprite in self.enemy1:
            if sprite.center_y > - 74:
                sprite.center_y -= 1

        for sprite in self.fire:
            shot_zombies = arcade.check_for_collision_with_list(sprite, self.enemy1)
            if shot_zombies:
                #arcade.play_sound(self.sound)
                self.score += len(shot_zombies)
                for extra_dead_zombies in shot_zombies:
                    self.enemy1.remove(extra_dead_zombies)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        fire = arcade.Sprite(":resources:images/space_shooter/laserRed01.png")
        fire.center_x = self.player.center_x
        fire.center_y = self.player.center_y + 74
        self.fire.append(fire)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -5
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 5
        if symbol == arcade.key.SPACE:
            fire = arcade.Sprite(":resources:images/space_shooter/laserRed01.png")
            fire.center_x = self.player.center_x
            fire.center_y = self.player.center_y + 74
            self.fire.append(fire)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_dx = 0


