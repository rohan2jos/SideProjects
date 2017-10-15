from kivy.app import App
from kivy.uix.button import Button

class KivyTest(App):
    def build(self):
        btn = Button(text="A Button",
                      font_size=100)
        btn.bind(on_press=self.callbackfunction)
        return btn

    def callbackfunction(self, instance):
        print "the button has just been pressed"

if __name__ == '__main__':
    KivyTest().run()