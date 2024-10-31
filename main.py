import pygame   #Importing modules
import time
import random
import os
from pygame import mixer
from GameElements import piece, Dice  
pygame.init()


win = pygame.display.set_mode((700,600))
pygame.display.set_caption("Kasy's Ludo Game")
clock = pygame.time.Clock()

#variables for the dice
number = random.randint(1,6)
second_number = random.randint(1,6)

# Sound and images
board = pygame.image.load(os.path.join("Assets", "images", "my ludo board.png"))
gojo = pygame.image.load(os.path.join("Assets","images","gojopic.jpg"))
dice_sound = mixer.Sound(os.path.join("Assets", "sounds","dice-on-a-wooden-floor-87441.mp3"))
kill_sound = mixer.Sound(os.path.join("Assets","sounds","thump-105302.mp3"))
movement_sound = mixer.Sound(os.path.join("Assets","sounds","Token Movement.wav"))



blue_positions = [(40,240),(80, 240), (120,240), (160,240), (200, 240),  (240, 200), (240,160), (240,120), (240,80), (240,40), (240,0), (280,0), #Blue to yellow
                 (320, 0), (320,40), (320,80), (320,120), (320,160), (320,200), (360,240), (400,240), (440,240), (480,240), (520,240),(560,240),(560,280), #yellow to purple
                 (560,320), (520,320), (480,320), (440,320), (400,320), (360,320), (320,360), (320,400), (320,440), (320,480), (320,520), (320,560), (280,560),  #purple to green 
                 (240,560), (240,520), (240,480), (240,440), (240,400), (240,360), (200,320), (160,320), (120,320), (80,320), (40,320), (0,320), (0,280)] #green to blue

yellow_positions = [(320,40), (320,80), (320,120), (320,160), (320,200), (360,240), (400,240), (440,240), (480,240), (520,240),(560,240),(560,280), #yellow to purple
                    (560,320), (520,320), (480,320), (440,320), (400,320), (360,320), (320,360), (320,400), (320,440), (320,480), (320,520), (320,560), (280,560),  #purple to green 
                    (240,560), (240,520), (240,480), (240,440), (240,400), (240,360), (200,320), (160,320), (120,320), (80,320), (40,320), (0,320), (0,280), #green to blue
                    (40,240),(80, 240), (120,240), (160,240), (200, 240),  (240, 200), (240,160), (240,120), (240,80), (240,40), (240,0), (280,0) ] #Blue to yellow

purple_positions = [(520,320), (480,320), (440,320), (400,320), (360,320), (320,360), (320,400), (320,440), (320,480), (320,520), (320,560), (280,560),  #purple to green 
                    (240,560), (240,520), (240,480), (240,440), (240,400), (240,360), (200,320), (160,320), (120,320), (80,320), (40,320), (0,320), (0,280), #green to blue
                    (40,240),(80, 240), (120,240), (160,240), (200, 240),  (240, 200), (240,160), (240,120), (240,80), (240,40), (240,0), (280,0), #Blue to yellow
                    (320, 0), (320,40), (320,80), (320,120), (320,160), (320,200), (360,240), (400,240), (440,240), (480,240), (520,240),(560,240),(560,280) ]#yellow to purple

green_positions = [(240,520), (240,480), (240,440), (240,400), (240,360), (200,320), (160,320), (120,320), (80,320), (40,320), (0,320), (0,280), #green to blue
                   (40,240),(80, 240), (120,240), (160,240), (200, 240),  (240, 200), (240,160), (240,120), (240,80), (240,40), (240,0), (280,0), #Blue to yellow
                   (320, 0), (320,40), (320,80), (320,120), (320,160), (320,200), (360,240), (400,240), (440,240), (480,240), (520,240),(560,240),(560,280), #yellow to purple
                   (560,320), (520,320), (480,320), (440,320), (400,320), (360,320), (320,360), (320,400), (320,440), (320,480), (320,520), (320,560), (280,560) ] #purple to green 

first_die = Dice(win, (240,270), number)
second_die = Dice(win, (300,270), second_number)

blue_piece1 = piece("purple", (40,40), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece2 = piece("purple", (40,120), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece3 = piece("purple", (120,40), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece4 = piece("purple", (120,120), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)

green_piece1 = piece("purple", (40,400), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece2 = piece("purple", (120,400), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece3 = piece("purple", (40,480), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece4 = piece("purple", (120,480), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)

yellow_piece1 = piece("purple", (400,40), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece2 = piece("purple", (480,40), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece3 = piece("purple", (400,120), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece4 = piece("purple", (480,120), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)

purple_piece1 = piece("purple", (400,400), win, os.path.join("Assets", "images", "purple.png"), purple_positions, movement_sound)
purple_piece2 = piece("purple", (480,400), win, os.path.join("Assets", "images", "purple.png"), purple_positions, movement_sound)
purple_piece3 = piece("purple", (400,480), win, os.path.join("Assets", "images", "purple.png"), purple_positions, movement_sound)
purple_piece4 = piece("purple", (480,480), win, os.path.join("Assets", "images", "purple.png"), purple_positions, movement_sound)

blue_pieces = [blue_piece1, blue_piece2, blue_piece3, blue_piece4]
yellow_pieces = [yellow_piece1, yellow_piece2, yellow_piece3, yellow_piece4]
green_pieces = [green_piece1,green_piece2,green_piece3,green_piece4]
purple_pieces = [purple_piece1,purple_piece2, purple_piece3, purple_piece4]

# all_pieces = []

# blue_piece = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)

turns = {1: "blue", 2:"yellow", 3:"purple", 4:"green"}
current_player = turns[1]


pieces = [blue_pieces, yellow_pieces, green_pieces, purple_pieces]

def handle_all_blits():
    win.fill("black")
    win.blit(gojo, (610,0))
    win.blit(board, (0,0))
    first_die.show_dice("Assets/images/1.png", "Assets/images/2.png", "Assets/images/3.png", "Assets/images/4.png", "Assets/images/5.png", "Assets/images/6.png")
    second_die.show_dice("Assets/images/1.png", "Assets/images/2.png", "Assets/images/3.png", "Assets/images/4.png", "Assets/images/5.png", "Assets/images/6.png")
    # blue_piece.create_piece()
    for all_pieces in pieces:
        for each_piece in all_pieces:
            each_piece.create_piece()


def handle_piece_movements():
    for all_pieces in pieces:
        for each_piece in all_pieces:
            if  mouse_pos[0] >= each_piece.current_pos[0] and mouse_pos[0] <= each_piece.current_pos[0] + 31:
                if mouse_pos[1] >= each_piece.current_pos[1] and mouse_pos[1] <= each_piece.current_pos[1] + 31:
                    number_to_move = first_die.get_number() - 1
                    each_piece.move(number_to_move, board)
                    # pygame.display.update()


#Main loop
running = True
while running:
    number = random.randint(1,6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        #  Dice roll
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 240 <= mouse_pos[0] <= 360 and 270 <= mouse_pos[1] <= 330:
                first_die.number = random.randint(1, 6)
                second_die.number = random.randint(1,6)
                dice_sound.play()
            handle_piece_movements()
            


    handle_all_blits()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()