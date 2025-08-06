from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.core.window import Window

from ocr_engine import extract_board_state
from ludo_ai import get_best_move

class LudoCoachApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.image = KivyImage(source='assets/board_sample.png')
        self.label = Label(text='📲 Tap below to analyze board', size_hint_y=0.2, color=(0,0,0,1))
        button = Button(text="Analyze Best Move", size_hint_y=0.2, background_color=(0.2, 0.6, 1, 1))
        button.bind(on_press=self.analyze_move)

        layout.add_widget(self.image)
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def analyze_move(self, instance):
        board = extract_board_state("assets/board_sample.png")
        move = get_best_move(board)
        self.label.text = f"🧠 Best Move:\n{move}"

if __name__ == '__main__':
    LudoCoachApp().run()
