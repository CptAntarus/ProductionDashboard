import pandas as pd
import matplotlib.pyplot as plt
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout
import io


class DataScreen(Screen):
    def on_enter(self):
        self.displayGraph()

    def displayGraph(self):
        # Read data
        df = pd.read_excel("ExcelTest.xlsx")
        grouped = df.groupby('data1')['data2'].mean()
        x = grouped.index.tolist()
        y = grouped.values.tolist()

        # Plot X/Y line graph
        plt.figure(figsize=(5, 3))
        plt.plot(x, y, marker='o', color='salmon', linestyle='-')
        plt.title('Data Line Graph')
        plt.xlabel('data1')
        plt.ylabel('Average of data2')
        plt.grid(True)
        plt.tight_layout()

        # Convert to texture
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        core_image = CoreImage(buf, ext='png')
        self.ids.dataImage.texture = core_image.texture

    def backToMenu(self):
        self.manager.current = 'menu'
