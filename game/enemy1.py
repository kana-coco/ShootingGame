import pygame
import random
from config import WIDTH, HEIGHT, COLORS, ENEMY_SPEED

# 🎯 修正: すべての敵クラスが pygame.sprite.Sprite を継承
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # pygame.sprite.Sprite の初期化を呼び出す
        self.size = 50
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(COLORS["green"])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.size)
        self.rect.y = 0

    def move(self):
        self.rect.y += ENEMY_SPEED

    def update(self):
        self.move()

# 速い敵
class FastEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image.fill(COLORS["red"])
        self.speed = ENEMY_SPEED * 2

    def move(self):
        self.rect.y += self.speed

# ジグザグ動く敵
class ZigzagEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image.fill(COLORS["blue"])
        self.direction = 1  # 左右の動き
        self.speed = ENEMY_SPEED

    def move(self):
        self.rect.y += self.speed
        self.rect.x += self.direction * 5  # 左右に動く
        if self.rect.x <= 0 or self.rect.x >= WIDTH - self.size:
            self.direction *= -1

# 弾を撃つ敵
class ShootingEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.image.fill(COLORS["purple"])

    def shoot(self, enemy_bullets):
        enemy_bullets.append(Bullet(self.rect.x + self.size // 2, self.rect.y + self.size))

# 🎯 修正: BossEnemy に Sprite の初期化を正しく追加
class BossEnemy(Enemy):
    def __init__(self):
        super().__init__()  # ここで Sprite の初期化を呼び出す
        self.size = 100
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(COLORS["black"])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.size)
        self.rect.y = 0
        self.health = 5

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()  # グループから削除
