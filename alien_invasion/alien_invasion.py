# coding=utf-8

import sys
import pygame
from settings import Settings

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 开始游戏主循环
    while True:
        # 监控键盘和鼠标事件
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
        # 让绘制可见
        pygame.display.flip()


run_game()
