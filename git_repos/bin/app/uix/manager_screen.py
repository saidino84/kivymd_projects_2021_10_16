from kivy.uix.screenmanager  import  ScreenManager
# from kivymd.uix.label import Label
from bin.app.uix.login import LoginPage
from bin.app.uix.game_screen import GamePage


class SManager(ScreenManager):
    # l=Label(text='hi')

    def on_kv_post(self,*k):
        self.add_widget(LoginPage(name='login'))
        # self.add_widget(GamePage(name='game_page'))
