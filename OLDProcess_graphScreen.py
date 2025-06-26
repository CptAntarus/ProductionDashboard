import pandas as pd
import matplotlib.pyplot as plt
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.image import Image as CoreImage
import io

# from kivy.lang import Builder
# Builder.load_file("FA_graphScreen.kv")

#df = pd.read_excel("ExcelTest.xlsx")

class GraphScreen(Screen):
    def on_enter(self):
        self.refreshGraph()

    def refreshGraph(self):
        df = pd.read_excel("ExcelTest.xlsx")

        grouped = df.groupby('data1')['data2'].mean()
        categories = grouped.index.tolist()
        values = grouped.values.tolist()

        plt.figure(figsize=(5, 3))
        plt.bar(categories, values, color='skyblue')
        plt.title('Sample Bar Graph')
        plt.xlabel('data1 (categories)')
        plt.ylabel('Average of data2')
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        core_image = CoreImage(buf, ext='png')
        self.ids.graphImage.texture = core_image.texture

    def backToMenu(self):
        self.manager.current = 'menu'
