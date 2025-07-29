from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from Waterfall import Waterfall

from PDG_GSM import GlobalScreenManager, GSM


class ActionsScreen(Screen):
    def on_enter(self):
        print("Made it to Actions Screen")

        print(GlobalScreenManager.CURRENT_PROCESS)
        print(GlobalScreenManager.CURRENT_TAG)

        self.ids.ActionsScreenTopBar.title = GlobalScreenManager.CURRENT_PROCESS
        grid = self.ids.actionsGrid
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
        print("Seclected Action: ", action)
