from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

"""
    Need to add option to read/save data for old reports 
    Maybe save to Excel sheet and use later.
"""

class GlobalScreenManager(ScreenManager):    
    REPORT_ID = 7567

    SCREEN_HIST = []

    TEMPLATE_REPORTS = [
        {"project": "Project 2", "tech": "Han Solo", "date": "05/04/2025"},
        {"project": "Project 3", "tech": "Chewbaca", "date": "06/02/2024"},
        {"project": "Project 1", "tech": "Luke Skywalker", "date": "12/02/2023"},
    ]


    # Product
    PROCESSES = [
        "C-130J AMU Tech Refresh 440400-000",
        "C-130J AMU Legacy 445500-000",
        "C-130J CMDU",
        "Apache 5x5",
        "Apache 6x6"
    ]

    def switchScreen(self, newScreen):
        GlobalScreenManager.SCREEN_HIST.append(self.current)
        self.current = newScreen


    def backButton(self, *args):
        self.current = GlobalScreenManager.SCREEN_HIST.pop()


def GSM():
    return MDApp.get_running_app().root
