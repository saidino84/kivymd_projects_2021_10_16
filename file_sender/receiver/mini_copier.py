from kivy.properties import NumericProperty,StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.button import *
from kivy.uix.relativelayout import RelativeLayout
import os,sys
from kivymd.toast import toast
from time import sleep
from kivymd.uix.snackbar import Snackbar
# from kivymd.uix.toast import toast
from kivymd.uix.filemanager import MDFileManager
class MiniCopier(FloatLayout):
    full=NumericProperty(0)
    angulo_inicial=NumericProperty(0)
    angulo_final=NumericProperty(0)
    angulo_max=NumericProperty(360)
    def __init__(self,**args):
        super(MiniCopier,self).__init__(**args)
        # self.animate_progress()
        self.manager_open=False
        self.filemanager=MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )



    def on_kv_post(self, base_widget):
        self.animate_progress()
        self.angulo_inicial=0
        print(self.angulo_final)
        # self.manager=MDFileManager(
        #     # previous=True,
        #     # exit_manager=self.exit_manager,
        #     # select_path=self.select_path
        #     )


    def animate_progress(self):
        a=Animation(radius=70, cor=(0.4,0.1,0,.0), w=7.,t='in_quad') + Animation(radius=60,cor=(.3,.55,.1,1),w=1.,t='out_quad')

        a.repeat=True
        a.start(self.ids['progress'])
        # self.animate_progress_(args)
        # print(args)

    def animate_progress_(self,*args):
        a=Animation(radius=50, d=args[0],t='out_quad')
        a.start(self.ids['progress'])

        # anim = Animation(...) + Animation(...)
        # anim.repeat = True
        # anim.start(widget)

    def choose_image(self):
        print('opening..')
        import os
        self.filemanager.show("/home/saidino/Desktop")
        print(os.path.dirname(os.path.abspath('__file__')))
        self.manager_open=True
    def select_path(self,path):
        self.exit_manager()
        # print(path, f'size : is {sys.getsizeof(path)}')
        im_size=os.path.getsize(path)
        file_name=path.split('/')[-1]
        # print(file_name,' Its [description]]  size é :',im_size)
        Snackbar(text=f"{file_name}  size {im_size}")
        item=ImageItem(source=path,size_=im_size,desc=file_name)
        self.ids['loaded_image'].clear_widgets()
        self.ids['loaded_image'].add_widget(item)
        self.ids['loaded_image'].is_loaded=True

        self.exit_manager()
        toast(path)
    def exit_manager(self,*args):
        self.manager_open=False
        self.filemanager.close()

    '''ULTIMATE FUNCIONS FOR MY APP '''
    def start_magic_saver(self):
        if self.ids['loaded_image'].is_loaded:
            self.angulo_final+=31
            if self.angulo_final>=100:

                self.angulo_final=self.angulo_max
                Animation.stop_all(self.ids['progress'])
                self.ids['progress'].cor=1,1,1,1
                self.ids['progress'].w=4.
                toast('Full uploaded_')
                Snackbar(text="Full uploaded ok?",button_text="BUTTON", button_callback=lambda x:toast('relaxe')).show()
        else:
            toast("Carregue uma image primeiro")
            Snackbar(text="Carregue uma image primeiro")


class ImageItem(RelativeLayout):
    source=StringProperty()
    _description=StringProperty()
    _im_size=NumericProperty()
    _im_desc=StringProperty()

    imag_size=NumericProperty()
    def __init__(self,source,size_,desc,**kwargs):
        super(ImageItem,self).__init__(**kwargs)
        self._source=source
        self._im_size=size_
        self._description=self.source.split('/')[-1]
        self.source=source
        self._im_siz=round(size_/1_048_576)
        self._im_desc=desc
        self.description=desc+' uploaded_'
        self.imag_size=size_

    def on_parent(self,parent,algo):
        print("SET SUCESSFULL")
        # self.imag_size=


    @property
    def description(self):
        nome=self._im_desc
        print('GETTING DESC')
        print(nome,' [x]')
        return nome#self._im_desc
    @description.setter
    def description(self,algo):
        print('SETTING DESCRI')
        self._im_desc=algo
        self.ids['image_des'].text=algo
        return self._im_desc

    @property
    def imag_size(self):
        size_img=self._im_size
        print('GETTING DESC')
        print(size_img,' image size [v]')
        return size_img#self._im_desc
    @imag_size.setter
    def imag_size(self,tamanho):
        print(f'SETTING IMAGE SIZE Bytes: {tamanho} ',end='')
        self._im_siz=tamanho/(1*1_048_576)
        print("EM MEGAS :",self._im_size)
        self.ids['image_siz'].text='{:.2} MB'.format(tamanho/1_048_576)
        return self._im_desc

    def remove_from_parent(self):self.parent.clear_widgets()


    ...
        #
