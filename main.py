import wx
import requests


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Game Finder')
        panel = wx.Panel(self)
        mainFrameSizer = wx.BoxSizer(wx.VERTICAL)

        self.textInput = wx.TextCtrl(panel, pos=(5, 5))
        mainFrameSizer.Add(self.textInput, 0, wx.ALL | wx.EXPAND, 5)

        enterBtn = wx.Button(panel, label="Enter", pos=(5, 55))
        enterBtn.Bind(wx.EVT_BUTTON, self.enterPress)
        mainFrameSizer.Add(enterBtn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(mainFrameSizer)
        self.Show()

    def enterPress(self, event):
        value = self.textInput.GetValue()
        if not value:
            print("Please enter the name of a Game first.")
        else:
            print(f"You are looking for {value}.")

    def jsonCaller():
        apiServerURL = "https://api.rawg.io/api/games/grand-theft-auto-v"

        response = requests.get(apiServerURL)

        # check if server response, then get json
        if response.status_code != 200:
            print("[-] Can't connect to API Server, please check URL or try again later.")
        else:
            print("[+] Successfully Connected to Server \n")
            dataJson = response.json()
            gameName = dataJson["name_original"]
            # description = dataJson["description_raw"]
            metacritic = dataJson["metacritic"]
            releaseDate = dataJson["released"]
            gameImg = dataJson["background_image"]

        print(gameName, metacritic, releaseDate, gameImg)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
