# Game Coins Collector
import pgzrun
from random import randint

# define window size
WIDTH = 800
HEIGHT = 600

# define variable
score = 0

# Create object
fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('blue')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score),color='red',topleft=(10,10))

def place_coin():
    coin.x = randint(20,(WIDTH - 20))
    coin.y = randint(20,(HEIGHT - 20))

def update():
    global score
    if keyboard.left :
        fox.x = fox.x - 4
       
    elif keyboard.right  :
        fox.x = fox.x + 4
        
    elif keyboard.up  :
        fox.y = fox.y - 4
        
    elif keyboard.down :
        fox.y = fox.y + 4
    
    elif fox.x > (800):
        fox.x = (1)
    
    elif fox.x < (1):
        fox.x = (800)
    
    elif fox.y > (600):
        fox.y = (1)
    
    elif fox.y < (1):
        fox.y = (600)
    
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1

pgzrun.go()