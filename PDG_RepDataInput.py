from kivy.uix.screenmanager import Screen

class RepDataInput(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def receiveReport(self, report):
        print("Made it to data input screen")
        print(report)