"""
开始菜单的通用按钮
"""

from common import uiBase
from common import resources
import pygame



class StartSceneBtn(uiBase.UIBase):
    """
    开始菜单的通用按钮类，继承自uiBase.UIBase
    """
    def __init__(self,
                 screen: pygame.Surface,
                 x: int,
                 y: int,
                 size: tuple,
                 color: tuple = (255,255,255),
                 text: str = "",
                 font_size: int = 16,
                 font_color:tuple | str = (0,0,0),
                 font_family: str = "font.ttf",
                 user_font_family = True,
                 center_anchor: bool = False
                ):
        """
        定义开始菜单的通用按钮，已经把字体定义好了
        :param screen: 绘制到该Surface
        :param x: UI的位置x
        :param y: UI的位置y
        :param size: UI的大小(width,height)
        :parameter color: (可选) UI上的背景颜色
        :parameter text: (可选) UI上的文本
        :parameter font_size: (可选) UI上的文本字体大小
        :parameter font_color: (可选) UI上的文本字体颜色
        :parameter font_family: (可选) 字体
        :parameter user_font_family: (可选) 是否使用用户自定义字体文件
        :parameter center_anchor: (可选) 是否以中心点为锚点
        """
        super().__init__(
                screen, x,y, size, color, text, font_size, font_color,
                        font_family = font_family,
                        user_font_family = user_font_family,
                        center_anchor = center_anchor
                        )
        # 加载按钮图片与点击音效
        self.btn_img = resources.MENU_ui_btn_img
        self.btn_press_img = resources.MENU_ui_btn_press_img
        self.hover_sound_effect = resources.EFFECT_hover
        self.press_sound_effect = resources.EFFECT_press
        # 设置音效音量
        self.press_sound_effect.set_volume(0.2)
        # 是否已经打开关联的 UI
        self.has_open_ui = False
        # 设置初始按钮图片
        self.set_background_image(self.btn_img)


    def _mouse_down(self, event:pygame.event.Event):
        self.opacity = 150
        # 父类处理事件必须放最后，否则子类方法会被覆盖
        super()._mouse_down(event)

    def _mouse_up(self, event:pygame.event.Event):
        self.opacity = 255
        self.press_sound_effect.play()
        # 父类处理事件必须放最后，否则子类的某些特殊方法会被覆盖
        super()._mouse_up(event)

    def _mouse_enter(self, event:pygame.event.Event):
        self.transition_scale(1.3, 1, 0.1)
        self.set_background_image(self.btn_press_img)
        self.set_text(font_color=(255, 255, 255), font_size=24)
        # 设置鼠标样式
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        self.hover_sound_effect.play()
        # 父类处理事件必须放最后，否则子类方法会被覆盖
        super()._mouse_enter(event)

    def _mouse_leave(self, event:pygame.event.Event):
        self.opacity = 255
        self.transition_scale(1, 1, 0.1)
        self.set_background_image(self.btn_img)
        self.set_text(font_color=(0, 0, 0), font_size=22)
        # 设置鼠标样式
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # 父类处理事件必须放最后，否则子类方法会被覆盖
        super()._mouse_leave(event)
