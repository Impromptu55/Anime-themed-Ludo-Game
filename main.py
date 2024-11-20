import pygame   #Importing modules   
import time
import random
import os
from pygame import mixer
from GameElements import piece, Dice  
pygame.init()

#I CHANGED THE DICE RANDINT NUMBERS 

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
font = pygame.font.SysFont("comicsans", 16)
movement_sound.set_volume(0.7)



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

blue_piece1 = piece("blue", (40,40), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece2 = piece("blue", (40,120), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece3 = piece("blue", (120,40), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)
blue_piece4 = piece("blue", (120,120), win, os.path.join("Assets","images", "blue.png"), blue_positions, movement_sound)

green_piece1 = piece("green", (40,400), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece2 = piece("green", (120,400), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece3 = piece("green", (40,480), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)
green_piece4 = piece("green", (120,480), win, os.path.join("Assets", "images", "green.png"), green_positions, movement_sound)

yellow_piece1 = piece("yellow", (400,40), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece2 = piece("yellow", (480,40), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece3 = piece("yellow", (400,120), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)
yellow_piece4 = piece("yellow", (480,120), win, os.path.join("Assets", "images", "yellow.png"), yellow_positions, movement_sound)

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

turns = ["blue", "yellow", "purple", "green"]
current_player = 0
dice_rolled = False


def next_turn():
    global current_player, next_player
    next_player = turns[current_player]
    current_player = (current_player + 1) % 4


def is_mouse_on_piece(mouse_pos, piece):
    return (mouse_pos[0] >= piece.current_pos[0] and mouse_pos[0] <= piece.current_pos[0] + 40 and
            mouse_pos[1] >= piece.current_pos[1] and mouse_pos[1] <= piece.current_pos[1] + 40)

    
pieces = [blue_pieces, yellow_pieces, purple_pieces, green_pieces]

def check_piece_home():
    for all_pieces in pieces:
        for each_piece in all_pieces:
            if each_piece.current_pos != each_piece.init_pos:
                each_piece.home = False

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
    font = pygame.font.SysFont("comicsans", 16)
    text = font.render(f"{next_player}'s turn", 1, "black")
    text_rect = text.get_rect(topleft=(610, 0))
    demo_text = font.render(str(dice_rolled), 1, "black")
    demo_text_rect = demo_text.get_rect(topleft=(610,30))
    win.blit(text, text_rect)
    win.blit(demo_text, demo_text_rect)
    # pygame.display.update(text_rect)      
    
def check_killed_pieces(each_piece: piece, pieces: list[list[piece]], current_pieces):
    other_players = pieces
    other_players.remove(current_pieces)
    for i in other_players:
        for j in i:
            if each_piece.current_pos == j.current_pos:
                j.go_back_home(kill_sound)
                each_piece.off_board = True
                break

# def check_winner():
#     for i in blue_pieces:
#         if sel

counter = 0
def handle_piece_movements():  
    global counter, dice_rolled, mouse_pos
    current_pieces = pieces[turns.index(next_player)]

    if all(current_pieces) and (first_die.get_number() != 6 and  second_die.get_number() != 6):
        next_turn()
        dice_rolled = False
        return
    for each_piece in current_pieces:
        if is_mouse_on_piece(mouse_pos, each_piece): 
            if each_piece.home:
                if all(current_pieces):
                    # TEST 
                    # if first_die.get_number() == 6 or second_die.get_number() == 6:
                    if first_die.get_number() == 6 and second_die.get_number() != 6:
                            each_piece.move(second_die.get_number(), board, pieces, first_die, second_die)
                            # check_killed_pieces(each_piece, pieces, current_pieces)
                            dice_rolled = False
                            next_turn()
                            break
                    if first_die.get_number() != 6 and second_die.get_number() == 6:
                            each_piece.move(first_die.get_number(), board, pieces, first_die, second_die)
                            # check_killed_pieces(each_piece, pieces, current_pieces)
                            dice_rolled = False
                            next_turn()
                            break
                    if first_die.get_number() == 6 and second_die.get_number() == 6:
                            counter += 1
                            each_piece.move(1 ,board, pieces, first_die, second_die)
                            # check_killed_pieces(each_piece, pieces, current_pieces)
                            break
                if counter == 1 and second_die.get_number() == 6:
                    counter = 0
                    each_piece.move(0, board, pieces, first_die, second_die)
                    # check_killed_pieces(each_piece, pieces, current_pieces)
                    dice_rolled = False
                    next_turn()
                    break
                elif counter == 0 and first_die.get_number() == 6:
                    counter += 1
                    each_piece.move(0, board, pieces, first_die, second_die)
                    # check_killed_pieces(each_piece, pieces, current_pieces)
                    each_piece.taken_die = True
                    break
                else:
                    print("You need a six to move this piece!!")
                    break
                # if piece is not at home movements
            elif each_piece.home == False: 
                if each_piece.taken_die == False: #if piece is moving for first time
                    if counter == 0:
                        counter += 1                        
                        each_piece.move(first_die.get_number() -1 , board, pieces, first_die, second_die)
                        # check_killed_pieces(each_piece, pieces, current_pieces)
                        each_piece.taken_die = True
                        break
                    elif counter == 1:
                        each_piece.move(second_die.get_number(), board, pieces, first_die, second_die)
                        # check_killed_pieces(each_piece, pieces, current_pieces)
                        dice_rolled = False
                        next_turn()
                elif each_piece.taken_die == True:
                    counter = 0
                    each_piece.move(second_die.get_number() - 1, board, pieces, first_die, second_die)
                    # check_killed_pieces(each_piece, pieces, current_pieces)
                    each_piece.taken_die = False
                    dice_rolled = False
                    next_turn()

                    # move_number = max(first_die.get_number(), second_die.get_number()) - 5
                    # each_piece.move(move_number, board, pieces, first_die, second_die)
                    # dice_rolled = False
                    # next_turn()

next_turn()
#Main loop
running = True
while running:
    check_piece_home()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        #  Dice roll
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # next_turn()
            if 240 <= mouse_pos[0] <= 360 and 270 <= mouse_pos[1] <= 330:
                if dice_rolled == False:
                    first_die.number = random.randint(1, 6)
                    second_die.number = random.randint(1,6)
                    dice_rolled = True
                    dice_sound.play()
            handle_piece_movements()


    handle_all_blits()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()