from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from bin.app.uix.canvas_only import  CanvasBasic
from bin.app.uix.canvasbasics.quicar import Quicar
from bin.app.uix.canvasbasics.canvas_basic_2 import CanvasBasic2

class GamePage(MDScreen):
    users=["saide","lord","gin"]
    px1=20
    py1=20
    def __init__(self,**kwargs):
        super(GamePage,self).__init__(**kwargs)


    # def on_kv_post(self,*args):
    #     self.px1=self.width/2
    #     self.py1=self.height/2
    def add_some_widget(self,id):
        container=self.ids['container']
        if(id==1):
            container.add_widget(CanvasBasic2())

    def goHome(self):
        self.manager.current='login_page'

    def girar(self,*arg):
        self.px1+=arg[0]+3
        # self.py1-=4
        print(arg)
        print(self.px1)
        self.ids['res'].text=f'{self.px1}'
        # self.ids['gammer'].x1=self.px1

    def update(self,*args):
        Clock.schedule_interval(self.girar,1)


class Tab(MDFloatLayout,MDTabsBase):
    ...




