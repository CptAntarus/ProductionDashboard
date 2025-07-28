# Library Imports
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

# Local Imports
from PDG_GSM import GlobalScreenManager

class CreateNewReport(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Creates the inital list
    def on_enter(self):
        self.processList = self.ids.processList
        self.processList.clear_widgets()

        for i in GlobalScreenManager.PROCESSES:
             process = OneLineListItem(
                 text=i,
                 on_release=lambda r=i: self.selectProject(r)
             )
             self.processList.add_widget(process)
        self.filterProcesses()

    def filterProcesses(self):
        self.updateList("")
        self.ids.prosSearchInput.bind(text=self.onTextSearch)

    def onTextSearch(self, instance, value):
        self.updateList(value)
    
    def updateList(self, searchText):
        container = self.ids.processList
        container.clear_widgets()

        for name in GlobalScreenManager.PROCESSES:
            if searchText.lower() in name.lower():
                item = OneLineListItem(
                    text=name,
                    on_release=lambda x=name: self.selectProject(x)
                )
                container.add_widget(item)

    def selectProject(self, name):
        print(f"Selected: {name}")
        

"""
    DONE =-= create text input
    DONE =-= create list
           /=> search options based on input
    DONE ={==> clear list
           \=> print list items that match    
    
"""