import re
# KivyMD Imports
from kivymd.app import MDApp
# Kivy Imports
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window

from Waterfall import Waterfall
from kivy.lang import Builder
Builder.load_file("PDG_Format.kv")

# myScreen Imports
from PDG_GSM import GlobalScreenManager, GSM
from PDG_StartScreen import StartScreen
from PDG_CreateNewReport import CreateNewReport
from PDG_EditOldReport import EditOldReport
from PDG_RepDataInput import RepDataInput
from PDG_ActionsScreen import ActionsScreen


class ProcessGui(MDApp):
    def build(self):
        Window.size = (1000, 700)

        self.sm = GlobalScreenManager()
        self.sm.add_widget(StartScreen(name='startScreen'))
        self.sm.add_widget(CreateNewReport(name='createNewReport'))
        self.sm.add_widget(EditOldReport(name='editOldReport'))
        self.sm.add_widget(RepDataInput(name='repDataInput'))
        self.sm.add_widget(ActionsScreen(name='actionsScreen'))

        self.sm.transition = NoTransition()
        self.theme_cls.theme_style = 'Dark'

        return self.sm
    
    
    def on_start(self):
        GlobalScreenManager.PROCESSES = Waterfall.InitDataSection("Processes")
        GlobalScreenManager.ACTIONS = Waterfall.InitDataSection("Actions")
        GlobalScreenManager.TITLES = Waterfall.InitDataSection("Titles")

        print("Processes: ", GlobalScreenManager.PROCESSES)
        print("Actions: ", GlobalScreenManager.ACTIONS)
        print("Titles: ", GlobalScreenManager.TITLES)

        GSM().switchScreen('startScreen')


if __name__ == '__main__':
    ProcessGui().run()
