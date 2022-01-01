from kivy.app import App
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFlatButton,MDFillRoundFlatButton
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton,MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput

class MyApp(MDApp,App):
    def build(self):
        self.title="NLP App"
        self.icon='logo-img.jpg'
        self.theme_cls.primary_palette= 'Pink'
        self.th_sc_layout = MDBoxLayout(orientation='vertical')
        self.label = MDToolbar(
            title="Simplified Calculator"

        )
        self.label.pos_hint = {"top": 1
                               }
        self.label.left_action_items = [[
            "menu", lambda x: True
        ]]
        self.label.right_action_items = [[
            "clock", lambda x: True
        ]]
        self.th_sc_layout.add_widget(self.label)

        self.operators = ['+', '-', '*', '/', '**', '%', '//']
        self.last_was_operator = None
        self.last_button = None

        self.input = TextInput(
            multiline=False, readonly=True, halign="right", font_size=40
        )
        ##Add Text input to the layout
        self.th_sc_layout.add_widget(self.input)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '+'],
            ['.', '0', 'C', '-'],
            ['**', '//', '%', '~']

        ]

        for i in buttons:
            self.h_layout = MDBoxLayout(padding=250)
            for label in i:
                btn = MDRoundFlatButton(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint_x=0.5,
                    on_press=self.on_button_press
                )

                self.h_layout.add_widget(btn)
            self.th_sc_layout.add_widget(self.h_layout)

        self.equal_button = MDFillRoundFlatButton(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5 }, on_press=self.on_solution,
        )
        self.th_sc_layout.add_widget(self.equal_button)
        return self.th_sc_layout

    def on_button_press(self, instance):
        current = self.input.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.input.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.input.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.input.text
        if text:
            solution = str(eval(self.input.text))
            self.input.text = solution
if __name__=='__main__':
    obj=MyApp()
    obj.run()
