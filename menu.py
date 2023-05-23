import pygame
from random import choice
import game

class TextInput:
    def __init__(self, x, y, width, height, label="", max_length=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.text = ""
        self.font = pygame.font.Font(None, height - 10)
        self.label = label
        self.label_font = pygame.font.Font(None, height // 2)
        self.active = False
        self.max_length = max_length

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box, activate it
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        # Reset the text input if the user clicks somewhere else
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
            else:
                # Limit the input to a certain number of characters
                if len(self.text) < self.max_length:
                    self.text += event.unicode

    def get_text(self):
        return self.text

    def draw(self, surface):
        # Draw the input box
        pygame.draw.rect(surface, self.color, self.rect, 2)
        # Draw the label
        label = self.label_font.render(self.label, True, pygame.Color('black'))
        surface.blit(label, (self.rect.x, self.rect.y - self.rect.height // 2))
        # Draw the text inside the input box
        text_surface = self.font.render(self.text, True, pygame.Color('black'))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


class Button:
    def __init__(self, x, y, width, height, text, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = pygame.Color('black')

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def pick_first(self, player1, player2):
        first = choice([player1, player2])
        message = f'First Player is {first}!'
        if first == player1:
            game.playerData.current_player = 1
        else:
            game.playerData.current_player = 2
        return message