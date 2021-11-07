from kivy.uix.widget import Widget
from kivy.graphics.instructions import  Canvas
from kivy.graphics.vertex_instructions import Line,Ellipse ,Ellipse,Rectangle
from kivy.graphics.context_instructions import  Color
from kivy.metrics import dp
# from kivy.clock import Clock
from kivy.properties import  Clock

class CanvasBasic2(Widget):
    #@overrided
    def on_size(self,*args):
        """triged when the window is changed its size /resized"""
        print(f'{self.width}')
        # vou centralzar a bola
        self.ball.pos=(self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)


    def __init__(self,**k):
        super().__init__(**k)
        self.ball_size=dp(50)
        # veloidades
        self.vx=dp(3)
        self.vy=dp(3)
        self.bouncing=False
        with  self.canvas:
            Color(1,.32,.23,1)
            Line(points=(100,100,400,500),width=2)
            Line(circle=(100,100,40),width=2)#width.height,radius
            Color(.1,.32,.23,1)
            Line(rectangle=(200,400,40,40),width=2)
            Color(.1,.2,.23,1)
            self.rect =Rectangle(pos=(200,220),size=(60,60))#filed rectangle
            Color(1,1,1,1)
            self.ball=Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
    