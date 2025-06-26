# KivyMD Imports
from kivymd.app import MDApp
from kivymd.uix.list import MDList, ThreeLineListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import GridLayout
# Kivy Imports
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image


from kivy.lang import Builder
Builder.load_file("Process_Format.kv")

# myScreen Imports
from Process_GSM import GlobalScreenManager
from Process_StartScreen import StartScreen
from Process_CreateNewReport import CreateNewReport
from Process_EditOldReport import EditOldReport
from Process_RepDataInput import RepDataInput


class ProcessGui(MDApp):
    def build(self):
        Window.size = (1000, 700)

        self.sm = GlobalScreenManager()
        self.sm.add_widget(StartScreen(name='startScreen'))
        self.sm.add_widget(CreateNewReport(name='createNewReport'))
        self.sm.add_widget(EditOldReport(name='editOldReport'))
        self.sm.add_widget(RepDataInput(name='repDataInput'))
        self.sm.transition = NoTransition()
        self.theme_cls.theme_style = 'Dark'
        self.sm.current = 'startScreen'

        return self.sm
    
    def switchScreen(self, newScreen, prevScreen):
        self.sm.PREVIOUS_SCREEN = prevScreen
        self.sm.current = newScreen

    def backButton(self, prevScreen):
        self.sm.current = self.sm.PREVIOUS_SCREEN


if __name__ == '__main__':
    ProcessGui().run()