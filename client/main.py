import client

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

import random

class MainScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"

        self.createPlayer("kivy" + str(random.randint(1, 99)))

        return Builder.load_file("kivy.kv")
    
    def createPlayer(self, name):
        self.player = client.Client(name)

    def sendCommand(self, text):
        commandList = {"create": self.player.create_room, "join": self.player.join_room, "players": self.player.get_players, "start": self.player.start_game, "exit": self.player.exit, "started": self.player.has_started}
        paramList = {"create": 0, "join": 1, "players": 0, "start": 0, "exit": 0, "started": 0}

        label = self.root.ids.screenManager.get_screen("mainScreen").ids.commandOutput
        
        params = []

        text = text.split(" ")
        command = text[0]

        if len(text) > 1:
            text.pop(0)
            params = text

        if command not in commandList:
            label.text = "Invalid Command"
            return
        
        if len(params) != paramList[command]:
            label.text = f"Invalid parameters!\n{command} takes {paramList[command]} parameter(s)!"
            return

        label.text = str(commandList[command](*params))

    # def selectList(self, caller, list):
    #     self.loginUniversityMenu = MDDropdownMenu(
    #         caller=caller,
    #         width_mult=4,
    #         background_color=get_color_from_hex("#383838"),
    #         position="center",
    #         items=[{"viewclass": "TwoLineListItem", "text": f"{uni[0]}", "secondary_text": f"{uni[1]}", "height": dp(65), "on_release": lambda uni=uni: self.loginUniversityMenuCb(uni, caller),} for uni in self.universities]
    #     )

app = MainApp()
if __name__ == "__main__":
    MainApp().run()