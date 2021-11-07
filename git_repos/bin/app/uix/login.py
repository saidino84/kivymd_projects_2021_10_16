from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import Clock
class LoginPage(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()

    def go_to_game_page(self,*arg):
        self.manager.current='game_page'

    def login(self,password):
        print(self.app)
        print(password.text)
        if password.text=='root':
            print('is you root')
            self.ids['login_res'].text='Well come saidino'
            self.ids['login_res'].theme_text_color='Secondary'
            Clock.schedule_once(self.go_to_game_page,4)
            
        else:
            print('you failed')
            self.ids['login_res'].text='You failed'
            self.ids['login_res'].theme_text_color='Error'
            
