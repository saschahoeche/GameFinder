import wx


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


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
