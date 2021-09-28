# Game Coins Collector
import pgzrun
from random import randint

# define window size
WIDTH = 800
HEIGHT = 600

# Create object
fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('blue')
    fox.draw()
    coin.draw()


def place_coin():
    coin.x = randint(20,(WIDTH - 20))
    coin.y = randint(20,(HEIGHT - 20))

def update():
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2
    
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()

pgzrun.go()