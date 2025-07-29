from kivy.uix.screenmanager import Screen

from PDG_GSM import GlobalScreenManager, GSM

class RepDataInput(Screen):
    def on_enter(self):
        print("Made it to data input screen")
        self.ids.RepDataInputTitle.title = GlobalScreenManager.CURRENT_REPORT

    def receiveReport(self):
        print(GlobalScreenManager.CURRENT_REPORT)