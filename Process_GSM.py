from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

"""
    Need to add option to read/save data for old reports 
    Maybe save to Excel sheet and use later.
"""

class GlobalScreenManager(ScreenManager):    
    REPORT_ID = 7567

    PREVIOUS_SCREEN = ""

    TEMPLATE_REPORTS = [
        {"project": "Project 2", "tech": "Han Solo", "date": "05/04/2025"},
        {"project": "Project 3", "tech": "Chewbaca", "date": "06/02/2024"},
        {"project": "Project 1", "tech": "Luke Skywalker", "date": "12/02/2023"},
    ]

    PROCESSES = [
        "Process 1",
        "Process 2",
        "Process 3",
        "Process 4",
        "Process 5",
        "Process 6",
        "Process 7",
        "Process 8",
        "Process 9",
        "Process 10",
        "Process 11",
        "Process 12",
        "Process 13",
        "Process 14",
        "Process 15",
        "Process 16",
        "Process 17",
        "Process 18",
        "Process 19",
        "Process 20",
        "Process 21",
        "Process 22",
        "Process 23",
        "Process 24",
        "Process 25",
        "Process 26",
        "Process 27",
        "Process 28",
        "Process 29",
        "Process 30",
    ]



def GSM():
    return MDApp.get_running_app().root
