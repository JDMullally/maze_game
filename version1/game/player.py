import pyglet, math
from pyglet.window import key
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

moving_up = [pyglet.resource.image("up_move1.png"),
          pyglet.resource.image("still_up.png"),
          pyglet.resource.image("up_move2.png"),
          pyglet.resource.image("still_up.png")]

moving_down = [pyglet.resource.image("down_move1.png"),
          pyglet.resource.image("still_down.png"),
          pyglet.resource.image("down_move2.png"),
          pyglet.resource.image("still_down.png")]

moving_left = [pyglet.resource.image("left_move1.png"),
          pyglet.resource.image("still_left.png"),
          pyglet.resource.image("left_move2.png"),
          pyglet.resource.image("still_left.png")]

moving_right = [pyglet.resource.image("right_move1.png"),
          pyglet.resource.image("still_right.png"),
          pyglet.resource.image("right_move2.png"),
          pyglet.resource.image("still_right.png")]

character_up = pyglet.resource.image("still_up.png")
character_down = pyglet.resource.image("still_down.png")
character_right = pyglet.resource.image("still_right.png")
character_left = pyglet.resource.image("still_left.png")


moving_up_animation = pyglet.image.Animation.from_image_sequence(moving_up, duration=0.2, loop=True)
moving_right_animation = pyglet.image.Animation.from_image_sequence(moving_right, duration=0.2, loop=True)
moving_down_animation = pyglet.image.Animation.from_image_sequence(moving_down, duration=0.2, loop=True)
moving_left_animation = pyglet.image.Animation.from_image_sequence(moving_left, duration=0.2, loop=True)


class Player():
    def __init__(self, game_width, game_height):
        super(Player, self).__init__(game_width, game_height)
        self.character_sprite = pyglet.sprite.Sprite(character_up)
        self.max_speed = 2
        self.hor_speed = 0
        self.vert_speed = 0

    def draw(self):
        self.character_sprite.draw()

    def update(self, dt):
        self.character_sprite.x += self.hor_speed
        self.character_sprite.y += self.vert_speed
        if self.character_sprite.x < 0:
            self.character_sprite.x = 0
        if self.character_sprite.x >= game_height - 50:
            self.character_sprite.x = game_height - 50

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_sprite.image = moving_up_animation
            self.vert_speed = self.max_speed
        elif symbol == key.LEFT:
            self.character_sprite.image = moving_left_animation
            self.hor_speed = -self.max_speed
        elif symbol == key.RIGHT:
            self.character_sprite.image = moving_right_animation
            self.hor_speed = self.max_speed
        elif symbol == key.DOWN:
            self.character_sprite.image = moving_down_animation
            self.vert_speed = -self.max_speed

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_sprite.image = character_up
            self.vert_speed = 0
        elif symbol == key.DOWN:
            self.character_sprite.image = character_down
            self.vert_speed = 0
        elif symbol == key.RIGHT:
            self.character_sprite.image = character_right
            self.hor_speed = 0
        elif symbol == key.LEFT:
            self.character_sprite.image = character_left
            self.hor_speed = 0