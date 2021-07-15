from kivy.config import Config
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '480')


from kivymd.color_definitions import colors

colors["Light"]["CardsDialogs"] = '27b3c7'
colors["Light"]["Background"] = '000000'

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.color_definitions import colors
from kivymd.uix.card import MDCard
from kivymd.toast import toast


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        # self.theme_cls.set_colors(
        #     "Yellow", "50", "50", "50", "Green", "50", "50", "50"
        # )

        return Builder.load_file('login.kv')
    
    
    def authorization_logger(self):
        toast('Test Kivy Toast')
        pass

    def authorization_clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    
    def authorization_forgot_password(self):
        pass

    

MainApp().run()        
