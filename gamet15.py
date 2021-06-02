# this game will demonstrate:
# one player object that can be manipulated around the screen using the up, down, left and right arrow keys
# Received help for left and right here https://stackoverflow.com/questions/11365052/moving-an-object-left-and-right
# three enemy objects that will move across the screen
# one prize object
# if the player collides with the enemy objects, they lose and the game ends
# if the player collides with the prize object, they win and the game ends

import pygame # calling upon the Pygame library for its functions
import random # calling upon random to generate random numbers

pygame.init()  # initialising the pygame module

# specifying the screen dimensions
screen_width = 1100
screen_height =700
screen = pygame.display.set_mode((screen_width,screen_height)) # setting the length and height as specified above using pygame functions
white = (255, 255, 255) # changing screen to white to match the characters' backgrounds
screen.fill(white) 
pygame.display.update()

# creating the player, enemies and prize and assigning an image to each
player = pygame.image.load(r"C:\Users\Kirsty\Dropbox\Kirsten Forrester-54038\Introduction to Programming\Task 15\game\mouse.jpg")
enemy1 = pygame.image.load(r"C:\Users\Kirsty\Dropbox\Kirsten Forrester-54038\Introduction to Programming\Task 15\game\cat-trimmy.png")
enemy2 = pygame.image.load(r"C:\Users\Kirsty\Dropbox\Kirsten Forrester-54038\Introduction to Programming\Task 15\game\cat2-trimmy.png")
enemy3 = pygame.image.load(r"C:\Users\Kirsty\Dropbox\Kirsten Forrester-54038\Introduction to Programming\Task 15\game\cat3-trimmy.png")
prize = pygame.image.load(r"C:\Users\Kirsty\Dropbox\Kirsten Forrester-54038\Introduction to Programming\Task 15\game\cheese-trimmy.png")

# ascertain the dimensions of the images so that we are aware of there presence on/off the screen
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

# store the positions of the player, enemies and prize as variables so that they may be manipulated
player_x_position = 100
player_y_position = 50

# start the enemies and prizes off screen
# random y co ordinate between 0 and the difference between the screen height and enemy height
enemy1_x_position = screen_width
enemy1_y_position = random.randint(0, screen_height - enemy1_height) 
enemy2_x_position = screen_width
enemy2_y_position = random.randint(0, screen_height - enemy2_height)
enemy3_x_position = screen_width
enemy3_y_position = random.randint(0, screen_height - enemy3_height)
prize_x_position = screen_width
prize_y_position = random.randint(0, screen_height - prize_height)

# checking to see if the up or down keys are being pressed
# seeing as the game starts without pressing, set them to False for now
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

while True:
    screen.fill(white) # clears the screen 
    screen.blit(player, (player_x_position, player_y_position)) # placing the player on the screen at co ordinates specified
    screen.blit(enemy1, (enemy1_x_position, enemy1_y_position))
    screen.blit(enemy2, (enemy2_x_position, enemy2_y_position))
    screen.blit(enemy3, (enemy3_x_position, enemy3_y_position))
    screen.blit(prize, (prize_x_position, prize_y_position))
    
    pygame.display.flip() # updating the screen 
    
    # this loops through events in the game
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT: # this  checks if the user is quitting, if so it exits the game
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:  # this checks if the user is pressing down a key

         # check if the key pressed is the one that we want (up/down)
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        if event.type == pygame.KEYUP: # this checks if the user is not pressing a key down
        
            # check if the key released is the one we want (up/down)
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
    
    # The coordinates of the top left corner of the game wondow is (0, 0).
    #  to move the player down, we increase the y position. 
    
    if keyUp == True:
        if player_y_position > 0 : # ensuring that the user does not move the player above the window i.e. y co ordinate greater than 0
            player_y_position -= 1
    if keyDown == True:
        if player_y_position < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            player_y_position += 1
    if keyLeft == True:
        if player_x_position > 0:
            player_x_position -= 1
    if keyRight == True:
        if player_x_position < screen_width - player_width:
            player_x_position += 1
    
    # Check for collision of the enemies or the prize with the player
    # To achieve above we need bounding boxes around the images of the player, enemies and prize
    # Where the boxes intersect, there is a collision
    
    # retrieving bounding box for the player, enemies and prize:
    playerBox = pygame.Rect(player.get_rect())
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy3Box = pygame.Rect(enemy3.get_rect())
    prizeBox = pygame.Rect(prize.get_rect())

    # the below updates the playerBox position to be the same as the player's, enemies' and prize's positions
    # this is to ensure the box is around the player/enemies/prize image 
    playerBox.top = player_y_position
    playerBox.left = player_x_position
    enemy1Box.top = enemy1_y_position
    enemy1Box.left = enemy1_x_position
    enemy2Box.top = enemy2_y_position
    enemy2Box.left = enemy2_x_position
    enemy3Box.top = enemy3_y_position
    enemy3Box.left = enemy3_x_position
    prizeBox.top = prize_y_position
    prizeBox.left = prize_x_position
    
   
    # checking to see if the player collides with any of the enemies
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose!") # display that the user has lost 
        pygame.quit() # quit the game
        exit(0) # close window


    # checking to see if the player collides with the prize
    if playerBox.colliderect(prizeBox):
        print("You win!") # display that the user has won
        pygame.quit() # quit the game
        exit(0) # clsoe woindow
    
 
# Make enemies and prize approach the player
    
    enemy1_x_position -= 0.15
    enemy2_x_position -= 0.20
    enemy3_x_position -= 0.25
    prize_x_position -= 0.2
    
    