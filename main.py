from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

KV = '''
BoxLayout:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0.07, 0.07, 0.08, 1  # #131314 Gemini Dark Background
        Rectangle:
            pos: self.pos
            size: self.size

    # Top Header Bar
    BoxLayout:
        size_hint_y: None
        height: '60dp'
        padding: ['16dp', '10dp']
        spacing: '10dp'
        
        Image:
            source: 'logo.png'  # Your custom logo
            size_hint_x: None
            width: '32dp'
        
        Label:
            text: "Sol-Plex Pro [color=7aafff]Thinking[/color]"
            markup: True
            font_size: '20sp'
            bold: True
            halign: 'left'
            valign: 'center'
            text_size: self.size

    # Main Scrollable Engine View
    ScrollView:
        BoxLayout:
            id: content_box
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: '16dp'
            spacing: '16dp'

            # Gemini Thinking Status Widget
            BoxLayout:
                id: thinking_card
                orientation: 'vertical'
                size_hint_y: None
                height: '48dp'
                padding: '12dp'
                canvas.before:
                    Color:
                        rgba: 0.12, 0.13, 0.15, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [12,]

                Label:
                    id: thinking_label
                    text: "✨ Sol-Plex Reasoning Engine Idle"
                    font_size: '14sp'
                    color: 0.6, 0.6, 0.65, 1
                    halign: 'left'
                    valign: 'center'
                    text_size: self.size

            # AI Output Bubble
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: '180dp'
                padding: '16dp'
                canvas.before:
                    Color:
                        rgba: 0.11, 0.11, 0.12, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [16,]

                Label:
                    id: output_text
                    text: "Ready to execute cognitive workflows. Tap 'Run Thought Process' to begin."
                    font_size: '15sp'
                    color: 0.9, 0.9, 0.92, 1
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'

    # Bottom Control Bar
    BoxLayout:
        size_hint_y: None
        height: '80dp'
        padding: '16dp'

        Button:
            text: "Run Thought Process"
            background_normal: ''
            background_color: 0.28, 0.53, 0.96, 1  # Gemini Blue accent
            font_size: '16sp'
            bold: True
            on_press: app.start_thinking()
'''

class SolPlexApp(App):
    def build(self):
        return Builder.load_string(KV)

    def start_thinking(self):
        thinking_label = self.root.ids.thinking_label
        output_text = self.root.ids.output_text
        
        thinking_label.text = "✨ Thinking (Analyzing state vectors & pipelines)..."
        output_text.text = ""
        
        # Simulate step-by-step thinking response
        Clock.schedule_once(lambda dt: self.update_thinking("✨ Synthesizing optimal solution..."), 1.2)
        Clock.schedule_once(lambda dt: self.render_response(), 2.5)

    def update_thinking(self, msg):
        self.root.ids.thinking_label.text = msg

    def render_response(self):
        self.root.ids.thinking_label.text = "✨ Thought Process Complete"
        self.root.ids.output_text.text = (
            "Sol-Plex Engine Execution Result:\n\n"
            "• Cognitive Graph: Operational\n"
            "• Memory Vectors: Synchronized\n"
            "• Status: Ready for continuous async deployment."
        )

if __name__ == "__main__":
    SolPlexApp().run()
