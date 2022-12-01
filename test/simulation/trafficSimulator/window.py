import pygame
from pygame import gfxdraw
import numpy as np

class Window:
    def __init__(self,sim,config={}):
        # 模拟绘制
        self.sim =sim

        # 设置默认配置
        self.set_default_config()

        # 更新配置
        for attr,val in config.items():
            setattr(self,attr,val)

    def set_default_config(self):
        self.width =1400
        self.height =900
        self.bg_color =(250,250,250)

        self.fps =60
        self.zoom =5
        self.offset =(0,0)

        self.mouse_last =(0,0)
        self.mouse_down =False

    def loop(self,loop=None):
        # 创建窗口
        self.screen =pygame.display.set_mode((self.width,self.height))
        pygame.display.flip()

        # 设置帧数
        clock =pygame.time.Clock()

        # 字体设置
        pygame.font.init()
        self.text_font =pygame.font.SysFont('Lucida Console',16)

        # 循环绘制
        running =True
        while running:
            # 暂时不清楚....
            if loop: loop(self.sim)
            # 仿真绘制
            self.draw()
            # 更新窗口
            pygame.display.update()
            clock.tick(slef.fps)
            # 事件处理
            for event in pygame.event.get():
                # 窗口关闭时结束循环
                if event.type ==pygame.QUIT:
                    running =False
                # 处理鼠标事件

    def run(self,steps_per_update=1):
        def loop(sim):
            sim.run(steps_per_update)
        self.loop(loop)

    # def convert(self):

    # def inverse_convert(self):
    #
    # def background(self):
    #
    # def line(self):
    #
    # def rect(self):
    #
    # def box(self):
    #
    # def circle(self):
    #
    # def polygon(self):
    #
    # def rotated_box(self):
    #
    # def rotated_rect(self):
    #
    # def arrow(self):
    #
    # def draw_axes(self):
    #
    # def draw_grid(self):
    #
    # def draw_roads(self):
    #
    # def draw_vehicle(self):
    #
    # def draw_vehicles(self):
    #
    # def draw_signals(self):
    #
    # def draw_status(self):
    #
    # def draw(self):
