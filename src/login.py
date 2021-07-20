from kivy.config import Config
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '480')


from kivymd.color_definitions import colors

colors["Light"]["CardsDialogs"] = '27b3c7'
colors["Light"]["Background"] = '000000'
colors["Light"]["FlatButtonDown"] = '000000'


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.color_definitions import colors
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from os import listdir


class UI(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        # self.theme_cls.set_colors(
        #     "Yellow", "50", "50", "50", "Green", "50", "50", "50"
        # )

        # more kv file
        # kv_path = "./kv_files/"
        # for kv in listdir(kv_path): 
        #     Builder.load_file(kv_path+kv) 

        Builder.load_file('login.kv')

        return UI()
    
    
    def authorization_logger(self):
        toast('Test Kivy Toast')
        pass

    def authorization_clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    
    def authorization_forgot_password(self):
        pass

    def exit(self):
        self.get_running_app().stop()   

    

MainApp().run()        
