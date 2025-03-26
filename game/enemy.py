import pygame
import random
from config import WIDTH, COLORS, ENEMY_SPEED

# 敵の種類(マロン(通常)、かなこ(速い敵)、はるくん(ジグザク敵)、拓哉(弾を撃ってくる敵)、お兄ちゃん(ボス)、お母さん(ボス)、お父さん(ボス))

# 敵のベースクラス
class Enemy:
    def __init__(self):
        self.size = 50
        self.rect = pygame.Rect(random.randint(0, WIDTH - self.size), 0, self.size, self.size)

    def move(self):
        self.rect.y += ENEMY_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, COLORS["green"], self.rect)

