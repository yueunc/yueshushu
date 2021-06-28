# coding=utf-8

import sys
import pygame
from settings import Settings


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    screen = Settings()
    # 设置背景色
    bg_color = (230, 230, 230)
    pygame.display.set_caption('Alien Invasion')
    # 开始游戏主循环
    while True:
        # 监控键盘和鼠标事件
        for event in pygame.event.get():
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
        # 让绘制可见
        pygame.display.flip()


run_game()
