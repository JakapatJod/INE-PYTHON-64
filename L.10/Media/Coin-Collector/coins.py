# Game Coins Collector
import pgzrun
from random import gammavariate, randint

# define window size
WIDTH = 800
HEIGHT = 600

# define variable
score = 0

game_over = False

# Create object
fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('pink')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score),color='red',topleft=(10,10))
    if game_over:
        screen.fill('black')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(100,50),color='red',fontsize=50)

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
    
    if fox.x > (800):
        fox.x = (1)
    
    if fox.x < (1):
        fox.x = (800)
    
    if fox.y > (600):
        fox.y = (1)
    
    if fox.y < (1):
        fox.y = (600)
    
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1
def time_up():
    global game_over
    game_over = True

clock.schedule(time_up,10.0)


place_coin()
pgzrun.go()