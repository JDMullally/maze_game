import pyglet
from pyglet import clock
from game import player
GAME_WIDTH = 800
GAME_HEIGHT = 800
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

bg = pyglet.resource.image('maze_background.png')

window = pyglet.window.Window(GAME_HEIGHT, GAME_WIDTH)
player = player.Player(GAME_WIDTH, GAME_HEIGHT)


@window.event
def on_draw():
    window.clear()
    bg.blit(0, 0)
    player.draw()


@window.event
def update(dt):
    player.update(dt)


@window.event
def on_key_press(symbol, modifiers):
    player.on_key_press(symbol, modifiers)


@window.event
def on_key_release(symbol, modifiers):
    player.on_key_release(symbol, modifiers)

clock.schedule_interval(update, 1 / 60.)

if __name__ == '__main__':
    pyglet.app.run()
