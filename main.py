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
        #  kljhbkljb

        return Builder.load_file('./libs/kv/login.kv')
    
    
    def authorization_logger(self):
        toast('Test Kivy Toast')
        pass

    def authorization_clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    
    def authorization_forgot_password(self):
        pass

    

MainApp().run()        


'''
==========================================
'''

# import kivy
# kivy.require('1.0.7')

# from kivy.app import App
# from kivy.uix.button import Button


# class TestApp(App):

#     def build(self):
#         # return a Button() as a root widget
#         return Button(text='hello world')


# if __name__ == '__main__':
#     TestApp().run()