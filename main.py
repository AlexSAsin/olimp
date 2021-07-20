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
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('src/main.kv')

from custom_graphics import CustomGraphics


sm = None
def set_sm(_sm):
    global sm
    sm = _sm
def get_sm():
    return sm

    

class VgxManaged(Widget):
    def _get_manager(self):
        return sm
    manager = property(_get_manager)


class CommonButton(Button):
    pass

class CommonHorizontalButton(CommonButton):
    pass

class MainScreen(Screen):
    pass

# ->

class InfoUserScreenUI(Screen):
    pass

class InfoUserScreen(VgxManaged):
    def select(self, val):
        print(val)

# <-

class PersonalAreaScreen(VgxManaged):
    pass
class PersonalAreaScreenUI(Screen):
    pass


class TrainingScreen(VgxManaged):
    pass
class TrainingScreenUI(Screen):
    pass

def get_checkbox_active():
    is_was_true = [False]
    def on_checkbox_active(check_box, val):
        # if is_was_true[0]:
        #     check_box.active = True
        #     return
        is_was_true[0] = True
        CustomGraphics.SetBG(
            check_box,
            bg_color=(0, 1, 0, .1) if val else (1, 0, 0, .5) 
        )
    return on_checkbox_active

class TaskScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(**kwargs)

        sv = ScrollView(do_scroll_x=False, do_scroll_y=True)
        
        main_box = BoxLayout()
        main_box.orientation = 'vertical'

        back_btn = CommonButton(text='Назад', size_hint_y=None, height=40)
        back_btn.bind(on_press=self._back_callback)


        main_box.add_widget(back_btn)
        main_box.add_widget(sv)

        self.add_widget(main_box)

        grid4sv = GridLayout(
            cols=1, row_force_default=True, row_default_height=200,
            size_hint=(1, None)
        )

        grid4sv.spacing = 10

        CustomGraphics.SetBG(self, bg_color=[0.02, 0.41, 0.41, 1.0])

        sv.add_widget(grid4sv)

        tasks = [
            ['Брасс', '200 м', '1'],
            ['Кроль', '4 х 50 м', '2', 'смена руки каждые 25м'],
            ['Кроль', '8 х 50 м', '3', 'Отдых 30 секунд'],
            ['Свободный', '200', ' 1']
        ]
        pre_title = ''
        pre_text = '  '
        font_size = 16
        parameters = {
            'halign':'left', 'size_hint_x': 1,'valign':'middle',
            'text_size':(225, None)
        }
        title_parameters = {
            'font_size': 17, 'bold': True
        }
        text_parameters = {
            'font_size': 15
        }

        for task in tasks:
            cur_task_el = BoxLayout(
                orientation='vertical',
                padding=[50, 0]
            )
            # cur_task_el.spacing = 20
            cur_task_el_wrapper = BoxLayout(
                orientation='vertical'
            )
            check_box = CheckBox(size_hint_y=None, height=20)
            check_box.bind(active=get_checkbox_active())

            CustomGraphics.SetBG(cur_task_el, bg_color=(0, 0, 0, .2, ))
            cur_task_el.add_widget(cur_task_el_wrapper)
            grid4sv.add_widget(cur_task_el)
            cur_task_el_wrapper.add_widget(check_box)
            cur_task_el_wrapper.add_widget(
                Label(text=pre_title + 'Стиль:', **parameters, **title_parameters)
            )
            cur_task_el_wrapper.add_widget(
                Label(text=pre_text + task[0], **parameters, **text_parameters)
            )
            cur_task_el_wrapper.add_widget(
                Label(text=pre_title + 'Дистанция:', **parameters, **title_parameters)
            )
            cur_task_el_wrapper.add_widget(
                Label(text=pre_text + task[1], **parameters, **text_parameters)
            )
            cur_task_el_wrapper.add_widget(
                Label(text=pre_title + 'Скорость:', **parameters, **title_parameters)
            )
            cur_task_el_wrapper.add_widget(
                Label(text=pre_text + task[2], **parameters, **text_parameters)
            )
            if len(task) > 3:
                # cur_task_el.size_hint_y = None
                # cur_task_el.height += 50
                cur_task_el_wrapper.add_widget(Label(
                    text=pre_title + 'Пометка:', **parameters, **title_parameters
                ))
                tm_lb = Label(text=pre_text + task[3], **parameters, **text_parameters)
                cur_task_el_wrapper.add_widget(
                    tm_lb
                )
                # CustomGraphics.SetBG(tm_lb, bg_color=(0, 0, 0, .2))

        grid4sv.height = grid4sv.row_default_height * 4 + grid4sv.spacing[0] * 3

    def _back_callback(self, btn):
        get_sm().current = 'personal_area'

            


class CompetitionsScreen(VgxManaged):
    pass
class CompetitionsScreenUI(Screen):
    pass


class TaskWrapper(BoxLayout):
    pass


# class TestApp(App):
#     def build(self):
#         # Create the screen manager
#         sm = ScreenManager()
#         sm.add_widget(MainScreen(name='main'))
#         sm.add_widget(InfoUserScreen(name='info_user')) ## !!!
#         sm.add_widget(PersonalAreaScreen(name='personal_area'))
#         sm.add_widget(TrainingScreen(name='training_screen'))
#         sm.add_widget(CompetitionsScreen(name='competitions_screen'))
#         sm.add_widget(TaskScreen(name='task_screen'))
#         return sm

class VgxMainScreen(VgxManaged):
    pass

class VgxUI(Screen):
    pass

class VgxApp(App):
    def build(self):
        set_sm(ScreenManager())
        sm = get_sm()
        sm.add_widget(TaskScreen(name='task_screen'))
        sm.add_widget(VgxUI(name='main'))
        sm.add_widget(InfoUserScreenUI(name='info_user'))
        sm.add_widget(PersonalAreaScreenUI(name='personal_area'))
        sm.add_widget(TrainingScreenUI(name='training_screen'))
        sm.add_widget(CompetitionsScreenUI(name='competitions_screen'))
        # print(competitions_screen)
        return sm

if __name__ == '__main__':
    VgxApp().run()