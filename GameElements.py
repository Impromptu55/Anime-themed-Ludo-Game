import pygame
import time
import random


class piece:
    def __init__(self, color:str, init_pos:tuple, win: pygame.Surface, image:str, positions:list, sound: pygame.mixer.Sound):
        self.color = pygame.Color(str(color))
        self.init_pos = init_pos
        self.win = win
        self.image = pygame.image.load(str(image)).convert()
        self.current_pos = self.init_pos
        self.position = positions
        self.moved = False
        self.sound = sound
        self.home = True

    def create_piece(self):
        if self.moved is False:
            self.win.blit(self.image, self.init_pos)
        elif self.moved is not False:
            self.win.blit(self.image, self.current_pos)
            


    def move(self, dice_number, background):
        self.moved = True
        tracking_list = self.position[0:dice_number]
        for i in tracking_list:
            self.win.blit(background, (0,0))
            time.sleep(0.05)
            self.win.blit(self.image, i)
            pygame.display.update()
            time.sleep(0.5)
            self.sound.play()
        self.current_pos = self.position[dice_number]
        self.position = self.position[dice_number:]
        self.sound.play()



class Dice:
    def __init__(self, win: pygame.Surface, init_pos: tuple, number: int):
        self.win = win
        self.init_pos = init_pos
        self.number = number
    
    
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

        
        