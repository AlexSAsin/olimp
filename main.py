import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('main.kv')


sm = None
def set_sm(_sm):
    global sm
    sm = _sm
def get_sm():
    return sm

class CommonButton(Button):
    pass

class CommonHorizontalButton(CommonButton):
    pass

class MainScreen(Screen):
    pass

class AuthScreen(Screen):
    pass

class PersonalAreaScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AuthScreen(name='auth'))
        sm.add_widget(PersonalAreaScreen(name='personal_area'))

        return sm

class VgxManaged(Widget):
    def _get_manager(self):
        return sm
    manager = property(_get_manager)

class VgxMainScreen(VgxManaged):
    pass

class VgxUI(Screen):
    pass

class VgxApp(App):
    def build(self):
        set_sm(ScreenManager())
        sm = get_sm()
        sm.add_widget(VgxUI(name='main'))
        sm.add_widget(AuthScreen(name='auth'))
        sm.add_widget(PersonalAreaScreen(name='personal_area'))
        return sm

if __name__ == '__main__':
    VgxApp().run()