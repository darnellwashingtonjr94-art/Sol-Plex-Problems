from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SolPlexApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Sol-Plex Engine Initialized", font_size='18sp')
        btn = Button(text="Run Sol-Plex Engine", size_hint=(1, 0.2))
        btn.bind(on_press=self.run_engine)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def run_engine(self, instance):
        self.label.text = "Executing Cognitive Engine..."

if __name__ == "__main__":
    SolPlexApp().run()
