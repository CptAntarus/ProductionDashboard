from kivy.uix.screenmanager import Screen

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        print("Oputput from StartScreen 7")
