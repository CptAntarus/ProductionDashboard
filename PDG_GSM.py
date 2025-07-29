from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

"""
    Need to add option to read/save data for old reports 
    Maybe save to Excel sheet and use later.
"""

class GlobalScreenManager(ScreenManager):
    CURRENT_PROCESS = 0
    CURRENT_TAG = 0
    CURRENT_REPORT = 0

    SCREEN_HIST = []

    TEMPLATE_REPORTS = [
        {"project": "C-130J AMU Tech Refresh 440400-000", "tech": "Han Solo", "date": "05/04/2025"},
        {"project": "C-130J AMU Legacy 445500-000", "tech": "Chewbaca", "date": "06/02/2024"},
        {"project": "C-130J CMDU", "tech": "Luke Skywalker", "date": "12/02/2023"},
    ]

    PROCESSES = {}
    ACTIONS = {}
    TITLES = {}


    def switchScreen(self, newScreen):
        GlobalScreenManager.SCREEN_HIST.append(self.current)
        self.current = newScreen


    def backButton(self, *args):
        self.current = GlobalScreenManager.SCREEN_HIST.pop()


    def reset(self):
        GlobalScreenManager.CURRENT_PROCESS = 0
        GlobalScreenManager.CURRENT_TAG = 0
        GlobalScreenManager.SCREEN_HIST.clear()


def GSM():
    return MDApp.get_running_app().root
