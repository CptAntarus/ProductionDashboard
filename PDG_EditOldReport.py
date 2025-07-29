from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineListItem
from PDG_GSM import GlobalScreenManager, GSM
from kivymd.uix.menu import MDDropdownMenu


class EditOldReport(Screen):
    def on_enter(self):
        self.populate_report_list()


    def populate_report_list(self, *args):
        report_data = GlobalScreenManager.TEMPLATE_REPORTS

        reportList = self.ids.reportList
        reportList.clear_widgets()

        for report in report_data:
            item = ThreeLineListItem(text="Project: " + report["project"],
                                    secondary_text="Tech: " + report["tech"],
                                    tertiary_text="Date: " + report["date"],
                                    on_release=lambda widget, r=report: self.selectReport(r))
            reportList.add_widget(item)


    def open_menu(self, item):
        sortOps = ["Project", "Tech", "Date"]
        menu_items = [
            {
                "text": i,"on_release": lambda x=i: self.sortOption(x),
            } for i in sortOps
        ]
        MDDropdownMenu(caller=item, items=menu_items).open()


    def sortOption(self, text_item):
        # Map displayed names to the keys in your report data
        key_map = {
            "Project": "project",
            "Tech": "tech",   
            "Date": "date"
        }

        sort_key = key_map.get(text_item, "project")

        report_data = sorted(GlobalScreenManager.TEMPLATE_REPORTS, key=lambda r: r[sort_key])

        # Refresh the list
        report_list = self.ids.reportList
        report_list.clear_widgets()
        for report in report_data:
            item = ThreeLineListItem(
                text="Project: " + report["project"],
                secondary_text="Tech: " + report["tech"],
                tertiary_text="Date: " + report["date"],
                on_release=lambda widget, r=report: self.selectReport(r)
            )
            report_list.add_widget(item)

        print(f"Sorted by: {sort_key}")


    def selectReport(self, report):
        print("Loading report: ", report["project"])
        GlobalScreenManager.CURRENT_REPORT = report["project"]

        GSM().switchScreen('repDataInput')