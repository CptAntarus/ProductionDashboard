# Library Imports
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

# Local Imports
from PDG_GSM import GlobalScreenManager, GSM

class CreateNewReport(Screen):
    # Creates the inital list
    def on_enter(self):
        self.processList = self.ids.processList
        self.processList.clear_widgets()

        for i in GlobalScreenManager.PROCESSES.keys():
             process = OneLineListItem(
                text=i,
                on_release=lambda widget, r=i: self.selectProject(r)
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


        for i in GlobalScreenManager.PROCESSES.keys():
            if searchText.lower() in i.lower():
                item = OneLineListItem(
                    text=i,
                    on_release=lambda widget, x=i: self.selectProject(x)
                )
                container.add_widget(item)
                print(i)


    def selectProject(self, name):
        print(name)
        print(GlobalScreenManager.PROCESSES[name])

        GlobalScreenManager.CURRENT_PROCESS = name
        GlobalScreenManager.CURRENT_TAG = GlobalScreenManager.PROCESSES[name]

        GSM().switchScreen('actionsScreen')