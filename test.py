# import pygame
import random

import pygame
import sys
import math

# 初始化Pygame
pygame.init()

# 设置窗口大小和标题
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("无人艇控制")

# 生成带栅格的白色地图
def draw_grid(surface, grid_size, color):
    for x in range(0, width, grid_size):
        pygame.draw.line(surface, color, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(surface, color, (0, y), (width, y))

# 加载无人艇图片并设置初始位置和旋转角度
boat_image = pygame.image.load(r'D:\python_work\reforcement_learning\maddpg-mpe-pytorch-master\无人艇.png')
boat_rect = boat_image.get_rect(center=(width // 2, height // 2))
boat_angle = 0
velocity = 0
rotation_speed = 0

# 主循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity += 1
            elif event.key == pygame.K_DOWN:
                velocity -= 1
            elif event.key == pygame.K_LEFT:
                rotation_speed = 5
            elif event.key == pygame.K_RIGHT:
                rotation_speed = -5
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                rotation_speed = 0

    # 更新无人艇位置和旋转角度
    boat_angle += rotation_speed
    boat_rect.x += velocity * math.cos(math.radians(boat_angle))
    boat_rect.y -= velocity * math.sin(math.radians(boat_angle))

    # 清屏并绘制地图和无人艇
    window.fill((255, 255, 255))
    draw_grid(window, 100, (200, 200, 200))

    # 旋转无人艇图像并绘制
    rotated_boat = pygame.transform.rotate(boat_image, boat_angle)
    new_rect = rotated_boat.get_rect(center=boat_rect.center)
    window.blit(rotated_boat, new_rect.topleft)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)

pygame.quit()
sys.exit()


# # 游戏窗口的宽度和高度
# WIDTH = 800
# HEIGHT = 600
#
# # 贪吃蛇方块的大小
# BLOCK_SIZE = 20
#
# # 定义颜色
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
#
# # 初始化Pygame
# pygame.init()
#
# # 创建游戏窗口
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("贪吃蛇")
#
# # 创建时钟对象，用于控制游戏的帧率
# clock = pygame.time.Clock()
#
# # 定义贪吃蛇的类
# class Snake:
#     def __init__(self):
#         self.length = 1
#         self.positions = [((WIDTH / 2), (HEIGHT / 2))]
#         self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
#         self.color = RED
#
#     def get_head_position(self):
#         return self.positions[0]
#
#     def update(self):
#         cur = self.get_head_position()
#         x, y = self.direction
#         new = (((cur[0] + (x*BLOCK_SIZE)) % WIDTH), (cur[1] + (y*BLOCK_SIZE)) % HEIGHT)
#         if len(self.positions) > 2 and new in self.positions[2:]:
#             self.reset()
#         else:
#             self.positions.insert(0, new)
#             if len(self.positions) > self.length:
#                 self.positions.pop()
#
#     def reset(self):
#         self.length = 1
#         self.positions = [((WIDTH / 2), (HEIGHT / 2))]
#         self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
#
#     def draw(self, surface):
#         for p in self.positions:
#             pygame.draw.rect(surface, self.color, (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))
#
# # 定义食物的类
# class Food:
#     def __init__(self):
#         self.position = (0, 0)
#         self.color = WHITE
#         self.randomize_position()
#
#     def randomize_position(self):
#         self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
#                          random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
#
#     def draw(self, surface):
#         pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))
#
# # 创建贪吃蛇和食物对象
# snake = Snake()
# food = Food()
#
# # 游戏循环
# running = True
# while running:
#     # 处理退出事件
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and snake.direction != (0, 1):
#                 snake.direction = (0, -1)
#             elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
#                 snake.direction = (0, 1)
#             elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
#                 snake.direction = (-1, 0)
#             elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
#                 snake.direction = (1, 0)
#
#     # 更新贪吃蛇和食物
#     snake.update()
#
#     if snake.get_head_position() == food.position:
#         snake.length += 1
#         food.randomize_position()
#
#     # 绘制游戏窗口
#     screen.fill(BLACK)
#     snake.draw(screen)
#     food.draw(screen)
#     pygame.display.update()
#
#     # 控制游戏帧率
#     clock.tick(10)
#
# # 退出游戏
# pygame.quit()
