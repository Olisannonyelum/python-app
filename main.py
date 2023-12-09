from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock

class ProgressPopup(Popup):
    def __init__(self, max_value, **kwargs):
        super(ProgressPopup, self).__init__(**kwargs)
        self.progress_bar = ProgressBar(max=max_value)
        self.content = BoxLayout(orientation='vertical') # tjs is the actual content property
        self.label_=Label(text="lies")
        self.content.add_widget(self.progress_bar)
        self.content.add_widget(self.label_)
        self.size_hint=None,None
        self.size=400,100

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        show_popup_button = Button(text='Show Popup', on_press=self.show_popup)
        layout.add_widget(show_popup_button)
        return layout

    def show_popup(self, instance):
        max_value = 100  # You can set your desired maximum value
        self.popup = ProgressPopup(max_value, title='Progress Popup')
        self.popup.open()

        # Simulate a task that updates the progress bar
        Clock.schedule_interval(self.update_progress, 1.0 / 30.0)

    def update_progress(self, dt):
        # Update the progress bar value here
        if self.popup.progress_bar.value < self.popup.progress_bar.max:
            self.popup.progress_bar.value += 1
        else:
            # Close the popup when the progress is complete
            self.popup.dismiss()
            Clock.unschedule(self.update_progress)

if __name__ == '__main__':
    MyApp().run()
