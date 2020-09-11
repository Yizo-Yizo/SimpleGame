import pygame 
import random 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("player.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 

game = True
keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.

while 1:  

    screen.fill(0) # Clears the screen.
    
    # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly. 
    
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0: 
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width: 
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies and a prize:

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.top = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy3Box):
        print("You lose!")   
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    if playerBox.colliderect(prizeBox) :
       print("You Win!")
       pygame.quit()
       exit(0)
        
    
#When the pictures are off the screen make them appear randomly again
    if enemy1XPosition < 0 - enemy1_width:
      
        enemy1XPosition =  screen_height
        enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

    if enemy2XPosition < 0 - enemy2_width:

        enemy2XPosition =  screen_height
        enemy2YPosition =  random.randint(0 , screen_height - enemy2_height)

    if enemy3XPosition < 0 - enemy3_width:

        enemy3XPosition =  screen_height
        enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

    if prizeXPosition < 0 - prize_width:

        prizeXPosition =  screen_height
        prizeYPosition =  random.randint(0, screen_height - prize_height)

    # Make enemy approach the player.
    
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15
    prizeXPosition -= 0.15
    
    # ================The game loop logic ends here. =============
  
