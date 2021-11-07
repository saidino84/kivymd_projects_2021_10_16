from kivy.uix.widget import Widget
from kivy.graphics.instructions import  Canvas
from kivy.graphics.vertex_instructions import Line,Ellipse ,Ellipse,Rectangle
from kivy.graphics.context_instructions import  Color
from kivy.metrics import dp
# from kivy.clock import Clock
from kivy.properties import  Clock
from kivymd.uix.button import MDRaisedButton

class Quicar(Widget):
    #@overrided
    def on_size(self,*args):
        """triged when the window is changed its size /resized"""
        print(f'{self.width}')
        # vou centralzar a bola
        self.ball.pos=(self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    # def on_touch_down(self,kv):
    #     print('start')
    #     self.start()
    def start_game(self,*args):
        print(f'check play: {self.opacity}')
        if(self.opacity==1):
            print('play started')
            self.start()
            return
        print('Unable to play')

    def __init__(self,**k):
        super().__init__(**k)
        self.ball_size=dp(50)
        # veloidades
        self.vx=dp(3)
        self.vy=dp(3)
        self.bouncing=False
        # self.add_widget(MDRaisedButton(text='Begin',id='btn',on_press=self.start))
        with  self.canvas:
            self.rect =Rectangle(pos=(200,220),size=(60,60))#filed rectangle
            Color(1,1,1,1)
            self.ball=Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
    
    def move(self,arg):
        x,y =self.rect.pos
        w,h=self.rect.size
        incrementer=dp(10)
        diff =self.width-(x+w)*2
        if(diff < incrementer):
            incrementer=diff

        x+=incrementer
        self.rect.pos =(x,y)
    def start(self):
        if(self.opacity==1):
        # Clock.schedule_interval(self.move,1/60)
            self.bouncing =not self.bouncing
            print(self.bouncing)
            if self.bouncing==True:
                Clock.unschedule(self.move_ball,1/60)
                self.ball.pos=self.center
                return
       
            Clock.schedule_interval(self.move_ball,1/60)
   
    def update_ui_txts(self,x,y):
        if(self.opacity==1):
            self.parent.ids['res'].text=f"""
            x:{x} y:{y} pos: {self.ball.pos}
            """
        else:
            self.parent.ids['res'].text=''

    def move_ball(self,dt):
        
        """TODO
            fazer abolar quicar se movendo nos
            eixos x e y e se passar fora do window do pai
            eles devem voltar pra atras
            VIDEO 2:21:10
        """
        x,y=self.ball.pos
        
        'QUANDO TOCAR EM CIMA'
        """se abola.y+size dele for maior que atela
            precisa contrariar decrementando o incrementador de posy do mesmo
            que eh vy
        """
        
        if y + self.ball_size > self.height:
            self.vy=-self.vy
        if x +self.ball_size >self.width:
            self.vx = -self.vx
        'QUANDO TOCAR NO CHAO'
        """se abola tocar no y do chao self.vy estava negativo e pra contrariar
            anegatividade dele para positivo preciso fazer 
            self.vy=-(self.vy)
            ex:vy=-10 then vy=-vy==+10
        """
        if x<0:
            x=0
            self.vx =-self.vx
        if y<0:
            y=0
            self.vy =-self.vy

        x+=self.vx
        y+=self.vy
        self.ball.pos=(x,y)      
        self.update_ui_txts(x,y)
