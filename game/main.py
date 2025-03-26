import pygame
import random
from config import WIDTH, HEIGHT, COLORS
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

# 画面サイズ設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("シューティングゲーム")

# FPS設定 (ゲームその速度をPCの性能に関わらず一定にするため)
clock = pygame.time.Clock()

# インスタンス作成
player = Player()
bullets = []
enemies = []

# メインループ
running = True
while running:
    screen.fill(COLORS["white"])  # 画面クリア

    # --- イベント処理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 弾を発射
                bullets.append(Bullet(player.rect.x + player.size // 2, player.rect.y))

    # --- キー入力処理 ---
    keys = pygame.key.get_pressed()
    player.move(keys)

    # --- 弾の移動 ---
    for bullet in bullets[:]:
        bullet.move()
        if bullet.rect.y < 0:
            bullets.remove(bullet)

    # --- 敵の生成 ---
    if random.randint(1, 50) == 1:
        enemies.append(Enemy())

    # --- 敵の移動 ---
    for enemy in enemies[:]:
        enemy.move()
        if enemy.rect.y > HEIGHT:
            enemies.remove(enemy)

    # --- 当たり判定（弾と敵）---
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # --- 画面描画 ---
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.flip()  # 画面更新
    clock.tick(30)  # FPS設定

pygame.quit()


