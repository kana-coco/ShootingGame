import pygame
from config import WIDTH, HEIGHT, COLORS, PLAYER_SPEED

class Player:
    def __init__(self):
        self.size = 50
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 60, self.size, self.size)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.size:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, COLORS["blue"], self.rect)
