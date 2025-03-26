import pygame
from config import WIDTH, HEIGHT, COLORS, PLAYER_SPEED

class Player:
    def __init__(self):
        self.size = 100
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 100, self.size, self.size)

        # プレイヤー画像の読み込み (assets/player.png)
        self.image = pygame.image.load("assets/かなた.jpg")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))  # サイズ調整
        self.image = self.make_circle(self.image)  # 丸くする

    def make_circle(self, image):
        """画像を丸く切り抜く"""
        # 透過付きの新しいサーフェス作成
        mask = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(mask, (255, 255, 255, 255), (self.size // 2, self.size // 2), self.size // 2)

        # 透明な背景の新しいサーフェスを作成
        result = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        result.blit(image, (0, 0))  # 画像をコピー
        result.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)  # 円形マスクを適用

        return result

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.size:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
