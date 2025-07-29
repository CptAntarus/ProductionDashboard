from kivy.uix.screenmanager import Screen

from PDG_GSM import GlobalScreenManager, GSM

class StartScreen(Screen):
    def on_enter(self):
        GlobalScreenManager().reset()
