from kivy.app import App
from kivy.uix.label import Label

class SolPlexApp(App):
    def build(self):
        return Label(text="Sol-Plex Engine Active")

if __name__ == "__main__":
    SolPlexApp().run()
