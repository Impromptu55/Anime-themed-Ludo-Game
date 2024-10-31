import pygame   #Importing modules
import time
import random
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
board = pygame.image.load("my ludo board.png")
gojo = pygame.image.load("gojopic.jpg")
dice_sound = mixer.Sound("dice-on-a-wooden-floor-87441.mp3")
kill_sound = mixer.Sound("thump-105302.mp3")
movement_sound = mixer.Sound("Token Movement.wav")



blue_positions = [(40,240),(80, 240), (120,240), (160,240), (200, 240),  (240, 200), (240,160), (240,120), (240,80), (240,40), (240,0), (280,0), #Blue to yellow
                 (320, 0), (320,40), (320,80), (320,120), (320,160), (320,200), (360,240), (400,240), (440,240), (480,240), (520,240),(560,240),(560,280), #yellow to purple
                 (560,320)]   

first_die = Dice(win, (240,270), number)
second_die = Dice(win, (300,270), second_number)

blue_piece1 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
blue_piece2 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
blue_piece3 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
blue_piece4 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)

green_piece1 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
green_piece2 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
green_piece3 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
green_piece4 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)

yellow_piece1 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
yellow_piece2 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
yellow_piece3 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
yellow_piece4 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)

purple_piece1 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
purple_piece2 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
purple_piece3 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)
purple_piece4 = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)

blue_pieces = [blue_piece1, blue_piece2, blue_piece3, blue_piece4]
yellow_pieces = [yellow_piece1, yellow_piece2, yellow_piece3, yellow_piece4]
green_pieces = [green_piece1,green_piece2,green_piece3,green_piece4]
purple_pieces = [purple_piece1,purple_piece2, purple_piece3, purple_piece4]

blue_piece = piece("purple", (40,40), win, "purple.png", blue_positions, movement_sound)


def get_currentplayer():
    global random_turn, current_player
    random_turn = True
    turns = ("blue", "yellow", "purple", "green")
    if random_turn == True:
        current_player = random.choice(turns)
        random_turn = False
        return current_player
    elif random_turn == False:
        former_player = current_player
        if former_player == "blue":
            current_player = "yellow"
        elif former_player == "yellow":
            current_player = "purple"
        elif former_player == "purple":
            current_player = "green"
        elif former_player == "green":
            current_player = "blue"
        return current_player



    


pieces = [blue_piece]

def handle_all_blits():
    win.fill("black")
    win.blit(gojo, (610,0))
    win.blit(board, (0,0))
    first_die.show_dice("1.png", "2.png", "3.png", "4.png", "5.png", "6.png")
    second_die.show_dice("1.png", "2.png", "3.png", "4.png", "5.png", "6.png")
    blue_piece.create_piece()


def handle_piece_movements():
    for all_pieces in pieces:
        if  mouse_pos[0] >= all_pieces.current_pos[0] and mouse_pos[0] <= all_pieces.current_pos[0] + 31:
            if mouse_pos[1] >= all_pieces.current_pos[1] and mouse_pos[1] <= all_pieces.current_pos[1] + 31:
                number_to_move = first_die.get_number() - 1
                all_pieces.move(number_to_move, board)
                # pygame.display.update()


#Main loop
running = True
while running:
    get_currentplayer()
    get_currentplayer()
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
    print(current_player)

pygame.quit()