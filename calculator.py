from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")

        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()

            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
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
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    app = MainApp()
    app.run()

# pip install kivy
# pip install buildozer -> in Linux OS: (instructions from https://realpython.com/mobile-app-kivy-python/)
    #  Create a new folder in your project and navigate into it with the cmd
    # ~$ buildozer init
    #  Configure buildozer.spec file with:
    """
    [app]
    
    # (str) Title of your application
    title = KvCalc
    
    # (str) Package name
    package.name = kvcalc
    
    # (str) Package domain (needed for android/ios packaging)
    package.domain = org.kvcalc
    """
    #  Install buildozer dependencies:
    """
    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv
    
    # add the following line at the end of your ~/.bashrc file
    export PATH=$PATH:~/.local/bin/
    """
    #  Copy your calculator application into your new folder and rename it to main.py.
    #  ~$ buildozer -v android debug
    """
    If everything goes according to plan, then you’ll have a file named something 
    like kvcalc-0.1-debug.apk in your bin folder.
    
    The next step is to connect your Android phone to your computer and copy the 
    apk file to it. Then you can open the file browser on your phone and click on 
    the apk file. Android should ask you if you’d like to install the application. 
    You may see a warning since the app was downloaded from outside Google Play, 
    but you should still be able to install it.
    """

