import pygame
import time


class piece:
    def __init__(self, color:str, init_pos:tuple, win: pygame.Surface, image:str, positions:list, sound: pygame.mixer.Sound):
        self.color = color
        self.init_pos = init_pos
        self.win = win
        self.image = pygame.image.load(str(image)).convert_alpha()
        self.current_pos = self.init_pos
        self.position = positions
        self.original_position = positions
        self.moved = False
        self.sound = sound
        self.home = True
        self.image.set_colorkey((255,255,255))
        self.taken_die = False
        self.taken_die_again = False
        self.off_board = False

    def __bool__(self):
        if self.home == True:
            return True
        else:
            return False

    def create_piece(self):
        if self.off_board == True:
            self.win.blit(self.image, (1000,1000))
            self.current_pos = (1000, 1000)
        elif self.moved is False:
            self.win.blit(self.image, self.init_pos)
        elif self.moved is not False:
            self.win.blit(self.image, self.current_pos)
            


    def move(self, dice_number, background, all_pieces, first_die, second_die):
        self.moved = True
        tracking_list = self.position[:dice_number]
        for i in tracking_list:
            self.win.blit(background, (0,0))
            for pieces in all_pieces:
                for each_piece in pieces:
                    if each_piece == self:
                        continue
                    each_piece.create_piece()
            first_die.show_dice("Assets/images/1.png", "Assets/images/2.png", "Assets/images/3.png", "Assets/images/4.png", "Assets/images/5.png", "Assets/images/6.png")
            second_die.show_dice("Assets/images/1.png", "Assets/images/2.png", "Assets/images/3.png", "Assets/images/4.png", "Assets/images/5.png", "Assets/images/6.png")
            time.sleep(0.05)
            self.win.blit(self.image, i)
            pygame.display.update()
            time.sleep(0.5)
            self.sound.play()
        try:
            self.current_pos = self.position[dice_number]
            self.position = self.position[dice_number+1:]
            self.sound.play()
        except IndexError as i:
            print(f"{i} has occurred but program will run!")

    def go_back_home(self,sound:pygame.mixer.Sound):
        self.current_pos = self.init_pos
        self.position = self.original_position
        sound.play()




class Dice:
    def __init__(self, win: pygame.Surface, init_pos: tuple, number: int):
        self.win = win
        self.init_pos = init_pos
        self.number = number
        self.taken = False
    
    
    def show_dice(self, a, b, c, d, e, f):
        dice_images = {1: pygame.image.load(str(a)),
                       2: pygame.image.load(b),
                       3: pygame.image.load(c),
                       4: pygame.image.load(d),
                       5: pygame.image.load(e),
                       6: pygame.image.load(f)}
        self.win.blit(dice_images[self.number], self.init_pos)    

    def get_number(self):
        return self.number

        
        