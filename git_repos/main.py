import os
from kivy.config import Config
# Config.set('graphics', 'width', '400')
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from bin.app.uix.login import LoginPage
from bin.app.uix.manager_screen import SManager
# Builder.load_file('main.kv')
# from kivy.uix.te



class GitApp(MDApp,App):
    KV_FILES ={
        os.path.join(os.getcwd(),'bin/app/kv/main.kv'),
        os.path.join(os.getcwd(),'bin/app/kv/login.kv'),
        os.path.join(os.getcwd(),'bin/app/kv/game.kv'),
    }
    CLASSES={
            "<SManager>":'bin/app/uix/manager',
            '<LoginPage>':'bin/app/uix/loginPage',
            "<GamePage>":'bin/app/uix/game_screen',
            "<CanvaBasic>":'bin/app/uix/canvas_only',
            "<Quicar>":'bin/app/uix/canvasbasics/quicar',
            "<CanvasBasic2>":'bin/app/uix/canvasbasics/canvas_basic_2'
            }
    AUTORELOADER_PATHS =[(os.getcwd(), {'recursive':True}),]
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style='Dark'

    def build_app(self):
        Window.bind(on_keyboard=self._rebuild)
        self.manager_screens =SManager()
        return self.manager_screens
    def _rebuild(self,*k):
        if k[1]==32:
            self.rebuild()


if __name__ == '__main__':
    GitApp().run()
