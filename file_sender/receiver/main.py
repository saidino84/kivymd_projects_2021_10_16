from kivymd.app import MDApp
from kaki.app import App
from kivy.uix.floatlayout import FloatLayout
import os
import importlib
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivymd.uix.card import MDCard
from kivy.core.window import Window

Window.size=(330,689)
# Window.rotation=90 #can rotate only 0, 90, 180, 270 degree
# Window.position=['custom'][0]
# Window.pos=(200,500,'d')



class LiveApp(App,MDApp):
    KV_FILES={
        os.path.join(os.getcwd(),'live.kv')
    }
    CLASSES ={
        'MiniCopier':'mini_copier'
    }
    AUTORELOADER_PATHS=[('.',{'recursive':True}),]

    def build_app(self):
        import mini_copier
        Window.bind(on_keyboard=self._rebuild)
        self.theme_cls.theme_style='Dark'
        importlib.reload(mini_copier)
        return mini_copier.MiniCopier()

    def _rebuild(self,*args):
        print("DEtected key {} ",format(args[1]))
        if args[1] ==32:
            self.rebuild()

LiveApp().run()
