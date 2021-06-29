# coding=utf-8

import sys
import pygame

from ship import Ship
from settings import Settings
import game_functions as gf


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建飞船
    ship = Ship(screen)
    # 开始游戏主循环
    while True:
        gf.click_events()
        gf.update_screen(ai_settings, screen, ship)
        pygame.display.flip()


run_game()
