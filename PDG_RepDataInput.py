from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton

from PDG_GSM import GlobalScreenManager, GSM


class RepDataInput(Screen):
    def on_enter(self):
        print("Made it to data input screen")
        self.ids.RepDataInputTitle.title = GlobalScreenManager.CURRENT_REPORT
        self.buildButtons()


    def buildButtons(self):
        grid = self.ids.EditOldReportGrid
        grid.clear_widgets()

        for action in GlobalScreenManager.ACTIONS.keys():
            if GlobalScreenManager.CURRENT_TAG in GlobalScreenManager.ACTIONS[action]:
                btn = MDRaisedButton(
                    text=action,
                    font_size="28sp",
                    on_release= lambda btn, A=action: self.selectOption(A)
                )
                grid.add_widget(btn)


    def selectOption(self, action):
        print(f"Selected Action: {action}")